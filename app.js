let connectMeButton = document.querySelector(".connect-me-button");
let connectMessage = "Dans la vie, y'a 2 types de personnes : les baiseurs et les baisés. ) à toi de voir, Roco."
let xhr = new XMLHttpRequest();

connectMeButton.addEventListener("click",()=>
{
    xhr.onreadystatechange = function()
    {
        if (xhr.response == 4)
        {
            console.log(xhr.response);
        }
    }
    xhr.open("GET", "server.php", true);
    xhr.send(connectMessage);
})