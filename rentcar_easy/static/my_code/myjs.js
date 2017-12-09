console.log("Hola Jorge");

// var DatatableRemoteAjaxDemo = function () {
//     var t = function () {
//         var t = $(".m_datatable_django").mDatatable({
//                 data: {

//                     ajax: {
//                         url: "https://editor.datatables.net/examples/php/join.php",
//                         type: 'POST'
//                     },
//                     pageSize: 10,
//                     saveState: {
//                         cookie: !0,
//                         webstorage: !0
//                     },
//                     serverPaging: !0,
//                     serverFiltering: !0,
//                     serverSorting: !0
//                 },
//                 layout: {
//                     theme: "default",
//                     class: "",
//                     scroll: !1,
//                     footer: !1
//                 },
//                 sortable: !0,
//                 pagination: !0,
//                 columns: [            { data: "users.first_name" },
//                 { data: "users.last_name" },
//                 { data: "users.phone" },
//                 { data: "sites.name" }]
//             }),
//             e = t.getDataSourceQuery();
//         $("#m_form_search").on("keyup", function (e) {
//             var a = t.getDataSourceQuery();
//             a.generalSearch = $(this).val().toLowerCase(), t.setDataSourceQuery(a), t.load()
//         }).val(e.generalSearch), $("#m_form_status").on("change", function () {
//             var e = t.getDataSourceQuery();
//             e.Status = $(this).val().toLowerCase(), t.setDataSourceQuery(e), t.load()
//         }).val(void 0 !== e.Status ? e.Status : ""), $("#m_form_type").on("change", function () {
//             var e = t.getDataSourceQuery();
//             e.Type = $(this).val().toLowerCase(), t.setDataSourceQuery(e), t.load()
//         }).val(void 0 !== e.Type ? e.Type : ""), $("#m_form_status, #m_form_type").selectpicker()
//     };
//     return {
//         init: function () {
//             t()
//         }
//     }
// }();
// jQuery(document).ready(function () {
//     DatatableRemoteAjaxDemo.init()
// });


$("#buscar").click(function(){

console.log("Hola");
});

$(document).ready(function() {

    $('#example').DataTable( {
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "scripts/server_processing.php",
            "data": function ( d ) {
  
                console.log(d);
            }
        }
    } );
} );