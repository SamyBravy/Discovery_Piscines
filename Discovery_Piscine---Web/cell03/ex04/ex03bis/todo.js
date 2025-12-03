function newElement()
{
    var todo = prompt("New TO DO:");

    if (todo != null && todo != '')
    {
        var newDiv = $("<div></div>");

        $(newDiv).click(deleteElement);
        $(newDiv).text('• ' + todo);
        $(newDiv).css('color', "blue");
        $(newDiv).css('padding', "10px");
        $(newDiv).css('font-size', "23px");
        $(newDiv).css('font-family', "comic sans ms");
        $(newDiv).css('text-align', "center");
        $(newDiv).css('overflow', "auto");
        $(newDiv).css('white-space', "nowrap");

        $('#ft_list').prepend(newDiv);
    }
}

function deleteElement()
{
    var userInput = confirm("Do you want to delete this TO DO?");

    if (userInput)
    {
        $(this).remove();
    }
}

addEventListener('beforeunload',
function(event)
{
    list = $('#ft_list').html();

    localStorage.setItem('list', list);
})

onload = function()
{
    list = localStorage.getItem('list');

    if (list)
    {
        $('#ft_list').html(list);
    }
}

addEventListener('keydown', function(event)
{
    if (event.key == "Delete")
    {
        $('#ft_list').html('');
    }
})
