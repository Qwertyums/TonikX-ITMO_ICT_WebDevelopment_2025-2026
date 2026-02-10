from django.urls import path

from .views import AllBookView, LibraryReaderView, LibraryReaderStatsView, YoungLibraryReaderStatsView, \
    ReaderReadingView, \
    BadReaderView, ReadingRareBook, MonthlyLibraryReportView, ConcreteBookView, ConcreteLibraryReaderView, \
    LibraryEmployeeUsernameView

urlpatterns = [
    # -------- КНИГИ --------
    path('books/', AllBookView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', ConcreteBookView.as_view(), name='book-delete'),

    # -------- ЧИТАТЕЛИ --------
    path('readers/', LibraryReaderView.as_view(), name='reader-list-create'),
    path('readers/<int:pk>/', ConcreteLibraryReaderView.as_view(), name='reader-delete'),

    # -------- СТАТИСТИКА ПО ЧИТАТЕЛЯМ --------
    path('readers/stats/education/', LibraryReaderStatsView.as_view(), name='reader-education-stats'),
    path('readers/stats/young/', YoungLibraryReaderStatsView.as_view(), name='young-readers-stats'),

    # -------- ЧТЕНИЕ --------
    path('readers/<int:reader_id>/books/', ReaderReadingView.as_view(), name='reader-books'),
    path('readers/bad/', BadReaderView.as_view(), name='bad-readers'),

    # -------- РЕДКИЕ КНИГИ --------
    path('readers/rare-books/', ReadingRareBook.as_view(), name='rare-book-readers'),

    # -------- ОТЧЁТ --------
    path('reports/monthly/<int:year>/<int:month>', MonthlyLibraryReportView.as_view(), name='monthly-library-report'),

    # -------- ПОЛЬЗОВАТЕЛИ --------
    path('library-employees/', LibraryEmployeeUsernameView.as_view(), name='employees-usernames'),
]
