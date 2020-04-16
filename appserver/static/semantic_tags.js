    $(document).ready(function () {
        var vals = ["Q18811437-Yunus"];
        vals.forEach(function (e) {
            if (!$ajax.find('option:contains(' + e + ')').length)
                $ajax.append($('<option>').text(e));
        });
        $ajax.val(vals).trigger("change");
    });

    var $ajax = $("#tags");
    function formatRepo(repo) {
        if (repo.loading) return repo.text;
        var markup = "<option id=" + repo.id + ">" + repo.id + "-" + repo.description + "<option>";
        return markup;
    }

    function formatRepoSelection(repo) {
        return repo.id;
    }
    $ajax.select2({
        ajax: {
            url: "https://www.wikidata.org/w/api.php?action=wbsearchentities&language=en&format=json&callback=?&",
            dataType: 'json',
            delay: 250,
            results: function (data, page) {
                return {
                    results: $.map(data.search, function (item) {
                        return {
                            id: item.id + "-" + item.label,
                            text: item.text
                        };
                    })
                };
            },
            multiple: true,
            data: function (params) {
                return {
                    search: params.term
                };
            },
            success: function (item) {

            },
            processResults: function (data, page) {
                return {
                    results: $.map(data.search, function (item) {
                        return {
                            id: item.id + "-" + item.label,
                            text: item.text,
                            description: item.description
                        };
                    })
                };
            },
            cache: true
        },
        escapeMarkup: function (markup) {
            return markup;
        },
        minimumInputLength: 3,
        templateResult: formatRepo,
        templateSelection: formatRepoSelection
    });