window.annotationCandidate = { target: ""};
window.savedAnnotations = [];
window.idCounter = 3;

annotationServerPort = 81
annotationServerRoot = "http://" + window.location.hostname + ":" + annotationServerPort


var annotationServerAuth = function (xhr) {
            var username = "admin";
            var password = "admin";
            xhr.setRequestHeader ("Authorization", "Basic " + btoa(username + ":" + password));
        }

function getPathTo(element) {
    // if (element.id !== '')
    //     return 'id("' + element.id + '")';
    if (element === document.body)
        return element.tagName;

    var ix = 0;
    var siblings = element.parentNode.childNodes;
    for (var i = 0; i < siblings.length; i++) {
        var sibling = siblings[i];
        if (sibling === element)
            return getPathTo(element.parentNode) + '/' + element.tagName + '[' + (ix + 1) + ']';
        if (sibling.nodeType === 1 && sibling.tagName === element.tagName)
            ix++;
    }
}
$.fn.xpathEvaluate = function (xpathExpression) {
   // NOTE: vars not declared local for debug purposes
   $this = this.first(); // Don't make me deal with multiples before coffee

   // Evaluate xpath and retrieve matching nodes
   xpathResult = this[0].evaluate(xpathExpression, this[0], null, XPathResult.ORDERED_NODE_ITERATOR_TYPE, null);

   result = [];
   while (elem = xpathResult.iterateNext()) {
      result.push(elem);
   }

   $result = jQuery([]).pushStack( result );
   return $result;
}


function resetAnnotations() {
    clearAnnotationHighlight();
    $(".text.saved-annotation").replaceWith(function () {return $(this).html()})
    $(".image.saved-annotation").remove();
    createSavedAnnotationsUi();
}
function clearAnnotationHighlight(){
    $("span.annotation-highlight").replaceWith(function () {return $(this).html()});
    $(".image-annotation-marker-candidate").remove();
    window.dispatchEvent(new CustomEvent("annotation-candidate-updated", {detail: { type: "text", annotationCandidateTarget: ""}}))
}
function createSavedAnnotationsUi(){
    window.savedAnnotations.forEach(function (ann){
        var target = $(document).xpathEvaluate("//" + ann.target.selector.value.split("|")[0]);
        if (ann.target.type == "TextualBody") {
            var selection = ann.target.selector.value.split("|")[1];
            var spn = '<span class="text saved-annotation" id="annotation-frame-' + ann.id + '">$1</span>';
            target.html(target.html().replace(new RegExp("(" + selection.replace(/\(/g, '\\(').replace(/\)/g, '\\)') + ")", "ig"), spn))
        }
        else if (ann.target.type == "Image") {
            var x = parseFloat(ann.target.selector.value.split("|")[1].split(",")[0]);
            var y = parseFloat(ann.target.selector.value.split("|")[1].split(",")[1]);
            target.append(
                $("<div>")
                .attr("id", "annotation-marker-" + ann.id)
                .addClass("image saved-annotation")
                .css({"position": "absolute", top: y, left: x})
                .click(function (event) {
                    event.stopPropagation();
                    $(".saved-annotation").removeClass("active");
                    $(this).addClass("active");
                    var annotation = window.savedAnnotations.filter(i => i.id === parseInt($(this).attr("id").split("-")[2]))[0];
                    var annotationBody = annotation.body.value;
                    var annotationAuthor = "Admin";

                    $("#new-annotation-form").hide();
                    $("#annotation-display").show();
                    $("#annotated-text>span").text("Image("+ parseInt(x)  + "," + parseInt(y) + ")");
                    $("#annotation-author").text("Author: " + annotationAuthor);
                    $("#annotation-body-display").text(annotationBody);

                    $(".ui.sidebar").sidebar("show");
                })
            )
        }
    })
}

window.addEventListener("annotation-candidate-updated", function (e) {
    window.annotationCandidate.target = e.detail.annotationCandidateTarget;
    window.annotationCandidate.targetType = e.detail.type;
    $("#annotating-text span").html(window.annotationCandidate.target != "" ?
        (window.annotationCandidate.targetType == "Image"?
            "Image(" + parseInt(window.annotationCandidate.target.split("|")[1].split(",")[0]) + "," + parseInt(window.annotationCandidate.target.split("|")[1].split(",")[1]) + ")"
            : window.annotationCandidate.target.split("|")[1]
        )
        :
        "<i class=\"fas fa-info-circle\"></i> <i>Select a target to annotate</i>");
    updateAnnotationModel();
    $("#annotation-body").prop("disabled", window.annotationCandidate.target == "");
    $("#create-annotation-button").prop("disabled", window.annotationCandidate.target == "");


})


// document.onclick = function (event) {
//     if (event === undefined) event = window.event;                     // IE hack
//     var target = 'target' in event ? event.target : event.srcElement; // another IE hack
//
//     var root = document.compatMode === 'CSS1Compat' ? document.documentElement : document.body;
//     var mxy = [event.clientX + root.scrollLeft, event.clientY + root.scrollTop];
//
//     var path = getPathTo(target);
//     var txy = getPageXY(target);
//     alert('Clicked element ' + path + ' offset ' + (mxy[0] - txy[0]) + ', ' + (mxy[1] - txy[1]));
// }



function getPageXY(element) {
    var x = 0, y = 0;
    while (element) {
        x += element.offsetLeft;
        y += element.offsetTop;
        element = element.offsetParent;
    }
    return [x, y];
}

function updateAnnotationModel(){
    window.annotationCandidate.annotationModel = `
{
  "@context": "http://www.w3.org/ns/anno.jsonld",
  "type": "Annotation",
  "body": {
    "type": "TextualBody",
    "value": "${window.annotationCandidate.body}",
    "format": "text/plain"
  },
  "target": {
    "source": "${window.location.href}",
    "type": "${window.annotationCandidate.targetType}",
    "selector": {
      "type": "XPathSelector",
      "value": "${window.annotationCandidate.target.replace(/"/g, '\'')}"
    }
  }
}
`
    $("#annotation-model pre").text(window.annotationCandidate.annotationModel);
    // $("#annotating-text span").text(window.annotationCandidate.target.split("|")[1]);
}

function fetchSavedAnnotations(){
    return $.ajax({
        // url: "http://localhost:8081/getAnnotations?url=" + window.location.href
        type: "GET",
        dataType: 'json',
        url: annotationServerRoot + "/annotations/",
        crossDomain: true,
        beforeSend: annotationServerAuth
    }).then(function(result) {
        var data = result.map(function (annObj) {
            var ann = JSON.parse(annObj.data);
            ann.id = annObj.id;
            ann.created =  annObj.created;
            return ann;
        });
        window.savedAnnotations = data.filter(function(ann) {return ann.target.source == window.location.href});
        resetAnnotations();
    });
}

$(document).ready(function () {

    fetchSavedAnnotations();

    $(".ui.sidebar")
        .sidebar({
            // context: "#page-content",
            transition: "overlay",
            dimPage: false,
            closable: false,
            onHide: function () {
                $(".saved-annotation").removeClass("active");
            },
            onShow: function () {
                $("#annotation-body").val("").focus();
            }
        }).on("click", function (event) {
        event.stopPropagation();
    })

    $("#close-sidebar").click(function () {
        $(".ui.sidebar").sidebar("hide");
    })

    $("#create-annotation-button").click(function () {
        $.ajax({
            type: "POST",
            url: annotationServerRoot + "/annotations/",
            dataType: 'json',
            contentType: 'application/json',
            crossDomain: true,
            beforeSend: annotationServerAuth,
            data: JSON.stringify({owner: 1, data: window.annotationCandidate.annotationModel})
        }).then(function(res) {
            var id = res.id
            resetAnnotations();
            fetchSavedAnnotations().then(function () {
                $(".saved-annotation").removeClass("active");
                $("#annotation-frame-"+id).addClass("active");
                var annotation = window.savedAnnotations.filter(i => i.id === id)[0];
                var annotatedText = annotation.target.type== "Image" ?
                    "Image(" + parseInt(annotation.target.selector.value.split("|")[1].split(",")[0]) + "," + parseInt(annotation.target.selector.value.split("|")[1].split(",")[1]) + ")"
                    : annotation.target.selector.value.split("|")[1];
                var annotationBody = annotation.body.value;
                var annotationAuthor = "Admin";

                $("#new-annotation-form").hide();
                $("#annotation-display").show();
                $("#annotated-text>span").text(annotatedText);
                $("#annotation-author").text("Author: " + annotationAuthor);
                $("#annotation-body-display").text(annotationBody);

                $(".ui.sidebar").sidebar("show");
            });

        });
    });

    $('<div class="ui popup" id="annotate-text-button">')
        .append('<button type="button" class="btn btn-outline-primary btn-lg"><i class="fa fa-comment"></i></button>')
        .on("click", function (event) {
            $(".saved-annotation").removeClass("active");
            event.stopPropagation();
            $("span.annotation-highlight").popup("hide");
            $("#new-annotation-form").show();
            $("#annotation-display").hide();
            $(".ui.sidebar").sidebar("show");
            $("#annotation-body").val("").focus();
        })
        .hide()
        .appendTo("body");

    $('<div class="ui popup" id="annotate-image-button">')
        .append('<button type="button" class="btn btn-outline-primary btn-lg"><i class="fa fa-comment"></i></button>')
        .on("click", function (event) {
            $(".saved-annotation").removeClass("active");
            event.stopPropagation();
            $("span.annotation-highlight").popup("hide");
            $("#new-annotation-form").show();
            $("#annotation-display").hide();
            $(".ui.sidebar").sidebar("show");
            $("#annotation-body").val("").focus();
        })
        .hide()
        .appendTo("body");


    $(document).on('click', function (event) {
        clearAnnotationHighlight();
        var target= 'target' in event? event.target : event.srcElement;
        var selection = window.getSelection(),
        span = document.createElement('span');
        span.className = 'annotation-highlight';

        var selectionRange = $(selection.anchorNode.parentNode).hasClass("annotatable") && selection.toString() != "" ?
                        selection.getRangeAt(0): undefined;
        // selectionRange.endContainer = selectionRange.startContainer
        if (selectionRange && $(selectionRange.endContainer.parentNode).hasClass("annotatable")){
            span.appendChild(selectionRange.extractContents());
            selectionRange.insertNode(span);
            var path = getPathTo(target);

            window.dispatchEvent(new CustomEvent("annotation-candidate-updated", {detail: { type: "TextualBody", annotationCandidateTarget: path + "|" + selection}}))

            $("span.annotation-highlight").popup({
                on: "hover", hoverable: true,
                popup: "#annotate-text-button",
                lastResort: 'top right',
                className: {
                    popup: "ui popup annotate-text-button"
                }
            })
        }
        else resetAnnotations();
    });
    $(document).on("click", ".text.saved-annotation", function (event) {
        event.stopPropagation();
        $(".saved-annotation").removeClass("active");
        $(this).addClass("active");
        var annotation = window.savedAnnotations.filter(i => i.id === parseInt($(this).attr("id").split("-")[2]))[0];
        var annotatedText = annotation.target.selector.value.split("|")[1];
        var annotationBody = annotation.body.value;
        var annotationAuthor = "Admin";

        $("#new-annotation-form").hide();
        $("#annotation-display").show();
        $("#annotated-text>span").text(annotatedText);
        $("#annotation-author").text("Author: " + annotationAuthor);
        $("#annotation-body-display").text(annotationBody);

        $(".ui.sidebar").sidebar("show");
    });
    $("#annotation-body").on("keyup", function (event) {
        window.annotationCandidate.body = $(this).val();
        updateAnnotationModel();
    });
    $("#annotation-body").trigger("keyup")

    $(".annotatable-image").on("click", function(event) {
        event.stopPropagation();
        $(".image-annotation-marker-candidate").remove();
        var bounds=this.getBoundingClientRect()
        var x = event.pageX - $(this).offset().left - 5;
        var y = event.pageY - $(this).offset().top - 5;
        var target= 'target' in event? event.target : event.srcElement;
        var path = getPathTo(target);
        $(this).append($("<div>").addClass("image-annotation-marker-candidate").css({"position": "absolute", top: y, left: x}))
        window.dispatchEvent(new CustomEvent("annotation-candidate-updated", {detail: { type: "Image", annotationCandidateTarget: path + "|" + x +"," + y}}))
        $(".image-annotation-marker-candidate").popup({
            on: "hover", hoverable: true,
            popup: "#annotate-image-button",
            lastResort: 'top right',
            className: {
                popup: "ui popup annotate-image-button"
            }
        })
    });
});