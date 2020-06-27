$("#targeton").click(function () {
    $.get('/test', function (data) {
        console.log(data);
    })
    // $.ajax({
    //     url: '/test',         /* Куда пойдет запрос */
    //     method: 'get',             /* Метод передачи (post или get) */
    //     dataType: 'json',          /* Тип данных в ответе (xml, json, script, html). */
    //     data: {text: 'Текст'},     /* Параметры передаваемые в запросе. */
    //     success: function (data) {   /* функция которая будет выполнена после успешного запроса.  */
    //         alert(data);            /* В переменной data содержится ответ от index.php. */
    //     }
    // });
});
$("#targetoff").click(function () {
    alert("Handler for .click() called.");
});
$("#home-button").click(function () {
    alert("Ты нажал на главную");
});
$("#parametrs-button").click(function () {
    alert("Ты нажал на параметры");
});
$("#errors-button").click(function () {
    alert("Ты нажал на ошибки");
});
$("#start-engine").click(function () {
    $.get('/test', function (data) {
        console.log(data);
    })
    alert("Ты нажал на start");
});
$("#stop-engine").click(function () {
    alert("Ты нажал на stop");
});
$("#change-car").click(function () {
    alert("Ты нажал на сменить машину");
});
$("#log-out").click(function () {
    alert("Ты нажал на выход");
});