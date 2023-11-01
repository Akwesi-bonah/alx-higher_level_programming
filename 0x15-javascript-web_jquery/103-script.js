$('document').ready(function () {
    $('INPUT#btn_translate').click(translate);
    $('INPUT#language_code').keypress(function (e) {
        if (e.which === 13) {
            translate();
        }
    });
    
});

function translate () {
    const url = 'https://www.fourtonfish.com/hellosalut/?lang=';
    const lang = $('INPUT#language_code').val();
    $.get(url + lang, function (data) {
        $('DIV#hello').text(data.hello);
    });
}