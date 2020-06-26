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