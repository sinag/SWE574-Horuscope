window.annotationCandidate = { target: ""};
window.idCounter = 3;
window.savedAnnotations = [
    {
      "@context": "http://www.w3.org/ns/anno.jsonld",
      "id": 1,
      "type": "Annotation",
      "body": {
        "type": "TextualBody",
        "value": "Annotation 1 Lorem ipsum dolor sit amet....",
        "format": "text/plain"
      },
      "target": {
        "source": "http://127.0.0.1:8000/instance/6",
        "selector": {
          "type": "XPathSelector",
          "value": "id('post-field-11')|Whatever I downed, it got me goin' crazy (Yah)"
        }
      }
    },
    {
      "@context": "http://www.w3.org/ns/anno.jsonld",
      "id": 2,
      "type": "Annotation",
      "body": {
        "type": "TextualBody",
        "value": "Annotation 2 Lorem ipsum dolor sit amet....",
        "format": "text/plain"
      },
      "target": {
        "source": "http://127.0.0.1:8000/instance/6",
        "selector": {
          "type": "XPathSelector",
          "value": "id('post-field-11')|Then a storm came in and saved my life"
        }
      }
    },
    {
      "@context": "http://www.w3.org/ns/anno.jsonld",
      "id": 3,
      "type": "Annotation",
      "body": {
        "type": "TextualBody",
        "value": "Annotation 3 - Date field Lorem ipsum dolor sit amet....",
        "format": "text/plain"
      },
      "target": {
        "source": "http://127.0.0.1:8000/instance/6",
        "selector": {
          "type": "XPathSelector",
          "value": "id('post-field-8')|2020-05-05T23:59:00"
        }
      }
    }
]

function getTextSelection() {
    var selection = window.getSelection();
    var annotatable = $(selection.anchorNode.parentNode).hasClass("annotatable");
    if (annotatable) {
        var highlightedText = selection.toString();
        return (highlightedText && highlightedText !== "") ? highlightedText.trim() : undefined;
    }
    return undefined;
    // var highlightedText = "";
    // if (window.getSelection) {
    //
    //     console.log(sel.anchorNode.parentNode);
    //     highlightedText = window.getSelection().toString();
    // } else if (document.selection && document.selection.type != "Control") {
    //     highlightedText = document.selection.createRange().text;
    // }
    // highlightedText = highlightedText.trim()
    // if (highlightedText && highlightedText !== "")
    //     return highlightedText;
    // return undefined;

}

function clearAnnotatorHighlight() {
    $("span.annotation-highlight").replaceWith(function () {
        return $(this).text()
    })
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

function getPathTo(element) {
    if (element.id !== '')
        return 'id("' + element.id + '")';
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
    "selector": {
      "type": "XPathSelector",
      "value": "${window.annotationCandidate.target.replace(/"/g, '\'')}"
    }
  }
}
    `;
    $("#annotation-model pre").text(window.annotationCandidate.annotationModel);
    $("#annotating-text span").text(window.annotationCandidate.target.split("|")[1]);
}

function createSavedAnnotationsUi(){
    $(".saved-annotation").replaceWith(function(){ return $(this).html();})
        window.savedAnnotations.forEach(function (ann){
        // var target = $(document).xpathEvaluate(ann.target.selector.value.split("|")[0]);
        var target = $("#" + ann.target.selector.value.split("|")[0].split("'")[1]);
        var selection = ann.target.selector.value.split("|")[1];
        var spn = '<span class="saved-annotation" id="annotation-frame-' + ann.id +'">$1</span>';
        target.html(target.html().replace(new RegExp("(" + selection.replace(/\(/g, '\\(').replace(/\)/g, '\\)') + ")", "ig"), spn))
    })
}

$(document).ready(function () {
    createSavedAnnotationsUi();

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
        debugger;
        var candidateAnnotation = JSON.parse(window.annotationCandidate.annotationModel);
        window.idCounter ++;
        candidateAnnotation.id = window.idCounter;
        window.savedAnnotations.push(candidateAnnotation);
        clearAnnotatorHighlight();
        createSavedAnnotationsUi();
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
        var selection = getTextSelection();
        clearAnnotatorHighlight()
        var target= 'target' in event? event.target : event.srcElement;
        if (selection) {
            var spn = '<span class="annotation-highlight">$1</span>';
            $(target).html($(target).html().replace(new RegExp("(" + selection.replace(/\(/g, '\\(').replace(/\)/g, '\\)') + ")", "ig"), spn))
            var path = getPathTo(target);

            window.annotationCandidate.target = path + "|" + selection;
            updateAnnotationModel();

            $(document).find("span.annotation-highlight").popup({
                on: "hover", hoverable: true,
                popup: "#annotate-text-button",
                lastResort: 'top right',
                className: {
                    popup: "ui popup annotate-text-button"
                }
            })
        }
        else{
            clearAnnotatorHighlight();
            // if (!$(target).hasClass("saved-annotation"));
            // $(".ui.sidebar").sidebar("hide");
        }
    });
    $(document).on("click", "span.saved-annotation", function (event) {
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
        $(".image-annotation-marker-candidate").remove();
        var bounds=this.getBoundingClientRect()
        var x = event.pageX - $(this).offset().left - 5;
        var y = event.pageY - $(this).offset().top - 5;
        $(this).append($("<div>").addClass("image-annotation-marker-candidate").css({"position": "absolute", top: y, left: x}))
        $(document).find(".image-annotation-marker-candidate").popup({
            on: "hover", hoverable: true,
            popup: "#annotate-image-button",
            lastResort: 'top right',
            className: {
                popup: "ui popup annotate-image-button"
            }
        })
    });
});