from charity_app.models import Category, Institution, Donation, User

c1 = Category.objects.create(name="Medycyna")
c2 = Category.objects.create(name="Pomoc sąsiedzka")
i1 = Institution.objects.create(name="WOŚP", description="medycyna dziecięca", type=1)
i2 = Institution.objects.create(name="Polskie Towarzystwo Stwardnienia Rozsianego - Oddział Wielkopolska",
                                description="medycyna dorosłych", type=2)
i3 = Institution.objects.create(name="Zbiórka choinek", description="sprzątanie po świętach", type=3)
i1.category.add(c1)
i2.category.add(c1)
i3.category.add(c2)

d1 = Donation.objects.create(quantity=1, address="Dominikańska 19C", phone_number=228523215, city="Warszawa",
                            zip_code="02738", pick_up_date="2020-02-22",pick_up_time="12:23:54",
                            pick_up_comment="ciesze się, że mogę pomóc", institution_id=1, user_id=1)

d1.categories.add(c1)
d1.institution.add(i1)

u1 = User.objects.create_user(username='Romek', first_name='Roman', last_name='Boczniak', email="rb@wp.pl",
                              password="rb")
