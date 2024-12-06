document.addEventListener("DOMContentLoaded", function () {
    console.log("Страница загружена");

    // Получаем модель
    var modal = document.getElementById("myModal");

    // Получаем элемент <span>, который закрывает модальный модуль
    var span = document.getElementsByClassName("close")[0];

    // Когда пользователь нажимает на члена команды, открывается модальный модуль
    var teamMembers = document.querySelectorAll(".team-member");
    teamMembers.forEach(function (member) {
      member.addEventListener("click", function () {
        var name = member.getAttribute("data-name");
        var role = member.getAttribute("data-role");
        document.getElementById("modalName").innerText = name;
        document.getElementById("modalRole").innerText = role;
        modal.style.display = "block";
      });
    });

    // Когда пользователь нажмет на <span> (x), закройте модальный модуль
    span.onclick = function () {
      modal.style.display = "none";
    };

    // Когда пользователь нажимает в любом месте за пределами модального меню, закрываем его
    window.onclick = function (event) {
      if (event.target == modal) {
        modal.style.display = "none";
      }
    };
});
