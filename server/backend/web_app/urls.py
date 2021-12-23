from django.urls import path
from . import web_menus, loans

urlpatterns = [

    path('menu/checkmenu/', web_menus.check_page, name="admin_check_page"),

    path('loan/list/', loans.list_record, name="loan_list"),
    path('loan/filter/', loans.list_filter, name="loan_filter"),
    path('loan/search/', loans.list_search, name="loan_search"),
    path('loan/download/', loans.download, name="loan_download"),
    path('loan/validate_id/', loans.preview, name="loan_preview"),
    path('loan/validate_data/', loans.validate_data, name="validate_data"),
    path('loan/loan_history/', loans.loan_history, name="loan_history"),
    path('loan/loan_check/', loans.check_previous_debt, name="check_previous_debt"),
    path('loan/loan_check_allow/', loans.allow_debtor, name="allow_debtor"),

]
