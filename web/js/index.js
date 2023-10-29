const ClearGalleryButton = document.getElementById("clear");

const BaseForm = `<form onsubmit="StableDiffusion(event)">
<input type="text" name="prompt" id="prompt">
<br>
<h5 style="text-align: center;">Выберите модель что бы сгенерировать</h5>
<br>
<input style="margin: auto; outline: none; border: none; border-radius: 5px;" class="btn" type="submit" value="Stable Diffusion">
</form>`;
const BaseWarning = `<div class="box"><h3>Нет подключение к интернету!</h3></div>`;

GetGallery();

async function GetGallery(){
    let galleryList = await eel.GetImages()();
    var count = document.getElementById("img-count");
    
    if(galleryList.length > 0){
        let htmlText = "";
        for (let i = 0; i < galleryList.length; i++) {
            galleryList[i] = galleryList[i].replace("./web/images", "");
            galleryList[i] = galleryList[i].replace("\\", "");
            galleryList[i] = galleryList[i].replace("\\", "");
            htmlText += `<img lazy class="gallery-img" src="./images/${galleryList[i]}">`;
        }
        document.getElementById("gallery").innerHTML = htmlText;
        ClearGalleryButton.style.display = "block";
        count.innerText = `Сгенерировано ${galleryList.length} картин`;
    }else{
        document.getElementById("gallery").innerHTML = "<h3>Тут пока нет сгенерированных картинок!</h3>";
        ClearGalleryButton.style.display = "none";
        count.innerText = "Нет картин";
    }
    return;
}

async function StableDiffusion(event){
    event.preventDefault();

    const input = document.getElementById("prompt"); 
    let prompt = input.value;
    if(prompt != null && prompt != ""){
        input.disabled = true;
        
        document.getElementById("msg").innerText = "Начало Stable Diffusion";

        let result = await eel.StableDiffusion(prompt)();
        if (result.status == true) {
            document.getElementById("msg").innerText = "Успешно сгенерировано! Смотрите в папке приложении!";
            setTimeout(() => {
                document.getElementById("msg").innerText = "";
            }, 4000);

            document.querySelector("#img").innerHTML = `<img style="width: 100%; height: 100%;" src="./images/${result.filename}.png">`;
        }else{
            document.getElementById("msg").innerText = "Произошла не предвиденная ошибка!";
            setTimeout(() => {
                document.getElementById("msg").innerText = "";
            }, 2000);
        }
        input.disabled = false;
        GetGallery();
        return;
    }
    document.getElementById("msg").innerText = "Текст пустой!";
    setTimeout(() => {
        document.getElementById("msg").innerText = "";
    }, 2000);
    
    return;
}

function ClearGallery(){
    var answ = prompt("Уверены? Это удалит все картинки из галлерии приложение! Напишите \"ДА\", что бы продолжить, или нажмите на отмену");
    if(answ == "ДА"){
        eel.ClearGallery();
        GetGallery();
        alert("Галлерея зачищена!");
    }
    return;
}

let prompter = document.getElementById("prompter");

async function CheckNetwork(){
    if (await eel.CheckNetwork()() == true) {
        if(prompter.innerHTML != BaseForm){
            prompter.innerHTML = BaseForm;
        }
    }else{
        if(prompter.innerHTML != BaseWarning){
            prompter.innerHTML = BaseWarning;
        }
    }
}

window.addEventListener("resize", function(){
    window.resizeTo(600, 525);
});

window.addEventListener("offline", function() {
    CheckNetwork();
});
window.addEventListener("online", function() {
    CheckNetwork();
});

CheckNetwork();
