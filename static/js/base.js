document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});
});

// モーダルウィンドウ※確認画面用
$(document).ready(function(){
    $('.modal').modal();
    // $('.modal-trigger').leanModal();
});

// 管理画面で削除id取得
$(document).on('click', '.delete-href', function(){
    deleteHref = "/sample_admin/" + $(this).data('id') + "/delete/";
    $("#delete-href").attr("href", deleteHref)
});
