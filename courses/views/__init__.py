from courses.views.homepage import HomePageView
from courses.views.courses import coursePage, MyCoursesList
from courses.views.auth import SignupView
from courses.views.auth import LoginView , signout
from courses.views.checkout import checkout , verifyPayment
from courses.views.new import newpage
from courses.views.searched import searchedPage
from courses.views.atoz import filteratoz
from courses.views.ztoa import filterztoa
from courses.views.pricelowtohigh import lowtohigh
from courses.views.pricehightolow import hightolow
from courses.views.forgotpassword import forgotpasswordPage
from courses.views.changepassword import changepasswordPage
from courses.views.cerificate import run_python_script