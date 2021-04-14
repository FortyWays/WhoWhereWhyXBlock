/* Javascript for WhoWhereWhyXBlock. */
function WhoWhereWhyXBlock(runtime, element) {

    function updateName(result) {
        $('.name', element).text(result.name);
        $('.email', element).text(result.email);
    }

    function updateCourse(result) {
        $('.course', element).text(result.course);
    }
    function updateQuote(result) {
        $('.insprirational-quote', element).text(result.quote);
    }


    var handlerWhoUrl = runtime.handlerUrl(element, 'who_handler');
    var handlerWhereUrl = runtime.handlerUrl(element, 'where_handler');
    var handlerWhyUrl = runtime.handlerUrl(element, 'why_handler');

    $('.who', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerWhoUrl,
            data: JSON.stringify({requested: 'name'}),
            success: updateName
        });
    });

    $('.where', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerWhereUrl,
            data: JSON.stringify({requested: 'course'}),
            success: updateCourse
        });
    });

    $('.why', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerWhyUrl,
            data: JSON.stringify({requested: 'inspiration'}),
            success: updateQuote
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
    return {};
}
