from django.urls import path
from . import widget, admin_menu, admin_web_menu, password, admin_privilege, itemcategory, \
    admin_account, user_account, userdata, loans, tester, contentcategory, statistics, dashboard, contents

urlpatterns = [
    path('tester/', tester.tests, name="tester"),
    path('statistics/', statistics.get_stats, name="statistics"),
    path('groups/', statistics.get_group, name="groups"),

    path('dashboard/list/', dashboard.list_record, name="dashboard_list"),
    path('dashboard/filter/', dashboard.list_filter, name="dashboard_filter"),
    path('dashboard/search/', dashboard.list_search, name="dashboard_search"),
    path('dashboard/download/', dashboard.download, name="dashboard_download"),
    path('dashboard/validate_id/', dashboard.preview, name="dashboard_preview"),

    path('adminmenu/menus/', admin_menu.menus, name="admin_menus"),
    path('adminmenu/checkmenu/', admin_menu.check_page, name="admin_check_page"),
    path('adminmenu/list/', admin_menu.list_record, name="admin_menu_list"),
    path('adminmenu/filter/', admin_menu.list_filter, name="admin_menu_filter"),
    path('adminmenu/search/', admin_menu.list_search, name="admin_menu_search"),
    path('adminmenu/download/', admin_menu.download, name="admin_menu_download"),
    path('adminmenu/validate_id/', admin_menu.preview, name="admin_menu_preview"),

    path('adminwebmenu/checkmenu/', admin_web_menu.check_page, name="admin_web_check_page"),
    path('adminwebmenu/list/', admin_web_menu.list_record, name="admin_menu_list"),
    path('adminwebmenu/filter/', admin_web_menu.list_filter, name="admin_menu_filter"),
    path('adminwebmenu/search/', admin_web_menu.list_search, name="admin_menu_search"),
    path('adminwebmenu/download/', admin_web_menu.download, name="admin_menu_download"),
    path('adminwebmenu/validate_id/', admin_web_menu.preview, name="admin_menu_preview"),

    path('adminprivilege/list/', admin_privilege.list_record, name="admin_privilege_list"),
    path('adminprivilege/filter/', admin_privilege.list_filter, name="admin_privilege_filter"),
    path('adminprivilege/search/', admin_privilege.list_search, name="admin_privilege_search"),
    path('adminprivilege/download/', admin_privilege.download, name="admin_privilege_download"),
    path('adminprivilege/validate_id/', admin_privilege.preview, name="admin_privilege_preview"),

    path('admin/list/', admin_account.list_record, name="admin_list"),
    path('admin/filter/', admin_account.list_filter, name="admin_filter"),
    path('admin/search/', admin_account.list_search, name="admin_search"),
    path('admin/download/', admin_account.download, name="admin_download"),
    path('admin/validate_id/', admin_account.preview, name="admin_preview"),

    path('user/list/', user_account.list_record, name="user_list"),
    path('user/filter/', user_account.list_filter, name="user_filter"),
    path('user/search/', user_account.list_search, name="user_search"),
    path('user/download/', user_account.download, name="user_download"),
    path('user/validate_id/', user_account.preview, name="user_preview"),

    path('widget/list/', widget.list_record, name="widget_list"),
    path('widget/filter/', widget.list_filter, name="widget_list_filter"),
    path('widget/search/', widget.list_search, name="widget_list_search"),
    path('widget/download/', widget.download, name="download_widget"),
    path('widget/validate_id/', widget.preview, name="widget_preview"),

    path('validate_password_id/', password.validate_password_id, name="validate_password_id"),

    path('userdata/getinfo/', userdata.get_user_profile, name="get_user_profile"),
    path('userdata/get_data/', userdata.user_data_session, name="user_data"),

    path('loan/list/', loans.list_record, name="loan_list"),
    path('loan/filter/', loans.list_filter, name="loan_filter"),
    path('loan/search/', loans.list_search, name="loan_search"),
    path('loan/download/', loans.download, name="loan_download"),
    path('loan/validate_id/', loans.preview, name="loan_preview"),
    path('loan/validate_data/', loans.validate_data, name="validate_data"),
    path('loan/loan_history/', loans.loan_history, name="loan_history"),
    path('loan/loan_check/', loans.check_previous_debt, name="check_previous_debt"),
    path('loan/loan_check_allow/', loans.allow_debtor, name="allow_debtor"),

    path('contentcategory/list/', contentcategory.list_record, name="content_category_list"),
    path('contentcategory/filter/', contentcategory.list_filter, name="content_category_filter"),
    path('contentcategory/search/', contentcategory.list_search, name="content_category_search"),
    path('contentcategory/download/', contentcategory.download, name="content_category_download"),
    path('contentcategory/validate_id/', contentcategory.preview, name="content_category_preview"),
    path('contentcategory/category/', contentcategory.category, name="content_category_category"),

    path('item_category/list/', itemcategory.list_record, name="item_category_list"),
    path('item_category/filter/', itemcategory.list_filter, name="item_category_filter"),
    path('item_category/search/', itemcategory.list_search, name="item_category_search"),
    path('item_category/download/', itemcategory.download, name="item_category_download"),
    path('item_category/validate_id/', itemcategory.preview, name="item_category_preview"),
    path('item_category/category/', itemcategory.category, name="item_category_category"),

    path('contents/list/', contents.list_record, name="contents_list"),
    path('contents/filter/', contents.list_filter, name="contents_filter"),
    path('contents/search/', contents.list_search, name="contents_search"),
    path('contents/download/', contents.download, name="contents_download"),
    path('contents/validate_id/', contents.preview, name="contents_preview"),

]
