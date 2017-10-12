var DatatableHtmlTableDemo = function () {
    var e = function () {
        var e = $(".m-datatable").mDatatable({
                columns: [{
                    field: "Deposit Paid",
                    type: "number"
                }, {
                    field: "Order Date",
                    type: "date",
                    format: "YYYY-MM-DD"
                }]
            }),
            a = e.getDataSourceQuery();
        $("#m_form_search").on("keyup", function (a) {
            e.search($(this).val().toLowerCase())
        }).val(a.generalSearch)
    };
    return {
        init: function () {
            e()
        }
    }
}();
jQuery(document).ready(function () {
    DatatableHtmlTableDemo.init()
});