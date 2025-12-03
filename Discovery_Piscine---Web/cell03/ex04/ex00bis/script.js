function changeBackground()
{
    var red = Math.floor(Math.random() * 256);
    var green = Math.floor(Math.random() * 256);
    var blue = Math.floor(Math.random() * 256);

    $('body').css('background-color', `rgb(${red}, ${green}, ${blue})`);
}