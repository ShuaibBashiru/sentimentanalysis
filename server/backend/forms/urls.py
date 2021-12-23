from django.urls import path
from . import views, admin_account, user_account, itemcategory, feedback, \
    password, admin_menu, web_menu, admin_privilege, loans, contentcategory

urlpatterns = [

    path('feedback/new/', feedback.addNew, name="feedback_new"),
    path('admin/new/', admin_account.addNew, name="admin_new"),
    path('admin/update/', admin_account.update, name="admin_update"),
    path('admin/update_status/', admin_account.update_status, name="admin_status"),
    path('admin/delete/', admin_account.delete, name="admin_delete"),

    path('user/new/', user_account.addNew, name="user_new"),
    path('user/update_status/', user_account.update_status, name="user_status"),
    path('user/delete/', user_account.delete, name="user_delete"),
    path('user/updatename/', user_account.updatename, name="updatename"),
    path('user/updatedob/', user_account.updatedob, name="updatedob"),
    path('user/updategender/', user_account.updategender, name="updategender"),
    path('user/updateemail/', user_account.updateemail, name="updateemail"),
    path('user/updatephone/', user_account.updatephone, name="updatephone"),
    path('user/updateaddress/', user_account.updateaddress, name="updateaddress"),
    path('user/updatepassword/', user_account.updatepassword, name="updatepassword"),
    path('user/jobrole/', user_account.jobrole, name="jobrole"),
    # path('user/passport/', user_account.passport, name="passport"),

    path('validate_email_id/', password.validate_email_id, name="validate_email_id"),
    path('update_password/', password.update_password, name="update_password"),

    path('adminmenu/new/', admin_menu.addNew, name="new_menu"),
    path('adminmenu/update/', admin_menu.update, name="update_menu"),
    path('adminmenu/update_status/', admin_menu.update_status, name="adminmenu_status"),
    path('adminmenu/delete/', admin_menu.delete, name="delete_menu"),

    path('adminwebmenu/new/', web_menu.addNew, name="web_menu"),
    path('adminwebmenu/update/', web_menu.update, name="update_web_menu"),
    path('adminwebmenu/update_status/', web_menu.update_status, name="web_menu_status"),
    path('adminwebmenu/delete/', web_menu.delete, name="delete_web_menu"),

    path('adminprivilege/update_status/', admin_privilege.update_status, name="admin_aprivilege_status"),
    path('adminprivilege/access/', admin_privilege.access, name="admin_access"),
    path('adminprivilege/delete/', admin_privilege.delete, name="delete_privilege"),

    path('loan/request_loan/', loans.new_request, name="new_request"),
    path('loan/update/', loans.update, name="update_loan"),
    path('loan/modify/', loans.modify_update, name="modify_update"),
    path('loan/update_status/', loans.update_status, name="loan_status"),
    path('loan/delete/', loans.delete, name="delete_loan"),

    path('category/new_category/', contentcategory.new_request, name="new_category"),
    path('category/update/', contentcategory.update, name="update_category"),
    path('category/update_status/', contentcategory.update_status, name="category_status"),
    path('category/delete/', contentcategory.delete, name="delete_category"),

    path('item_category/new_category/', itemcategory.new_request, name="new_category"),
    path('item_category/update/', itemcategory.update, name="update_item_category"),
    path('item_category/update_status/', itemcategory.update_status, name="itemcategory_status"),
    path('item_category/delete/', itemcategory.delete, name="delete_item"),

]
