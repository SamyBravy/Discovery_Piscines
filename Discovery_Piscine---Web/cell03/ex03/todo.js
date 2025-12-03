function newElement()
{
            
    var todo = prompt("New TO DO:");

    if (todo != null && todo != '')
    {
        var newDiv = document.createElement("div");

        newDiv.onclick = deleteElement;
        newDiv.textContent = '• ' + todo;
        newDiv.style.color = "blue";
        newDiv.style.padding = "10px";
        newDiv.style.fontSize = "23px";
        newDiv.style.fontFamily = "comic sans ms";
        newDiv.style.textAlign = "center";
        newDiv.style.overflow = "auto";
        newDiv.style.whiteSpace = "nowrap";

        document.getElementById("ft_list").prepend(newDiv);
    }
}

function deleteElement()
{
    var userInput = confirm("Do you want to delete this TO DO?");

    if (userInput)
    {
        this.remove();
    }
}

addEventListener('beforeunload',
function(event)
{
    list = document.getElementById("ft_list").innerHTML;

    localStorage.setItem('list', list);
})

onload = function()
{
    list = localStorage.getItem('list');

    if (list)
    {
        document.getElementById("ft_list").innerHTML = list;
    }
}

addEventListener('keydown', function(event)
{
    if (event.key == "Delete")
    {
        document.getElementById("ft_list").innerHTML = '';
    }
})
