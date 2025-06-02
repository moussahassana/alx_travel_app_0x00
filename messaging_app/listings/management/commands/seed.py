import random
from datetime import timedelta, date
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing, Booking, Review

User = get_user_model()

def random_date():
    start = date.today() + timedelta(days=random.randint(1, 10))
    end = start + timedelta(days=random.randint(2, 7))
    return start, end

class Command(BaseCommand):
    help = "Seed the database with sample data: listings, bookings, reviews"

    def handle(self, *args, **kwargs):
        # Ensure at least 2 users exist
        users = list(User.objects.all())
        if len(users) < 2:
            demo_users = [
                {"username": "demo_user1", "email": "demo1@example.com"},
                {"username": "demo_user2", "email": "demo2@example.com"},
            ]
            for user_info in demo_users:
                user, created = User.objects.get_or_create(
                    username=user_info["username"],
                    defaults={"email": user_info["email"]}
                )
                if created:
                    user.set_password("password123")
                    user.save()
                    self.stdout.write(self.style.SUCCESS(f"Created user: {user.username}"))
                users.append(user)
        else:
            self.stdout.write(self.style.WARNING("Using existing users."))

        host = users[0]
        other_user = users[1]

        # Clear previous data before seeding
        Review.objects.all().delete()
        Booking.objects.all().delete()
        Listing.objects.all().delete()

        # Seed Listings
        listings = []
        for i in range(5):
            listing = Listing.objects.create(
                title=f"Listing {i + 1}",
                description="A great place to stay.",
                price_per_night=random.randint(50, 300),
                address=f"{i+1} Main Street",
                host=host
            )
            listings.append(listing)
            self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))

        # Seed Bookings & Reviews for each listing
        for listing in listings:
            for _ in range(2):
                start_date, end_date = random_date()
                booking = Booking.objects.create(
                    listing=listing,
                    user=other_user,
                    start_date=start_date,
                    end_date=end_date
                )
                self.stdout.write(self.style.SUCCESS(
                    f"Booking from {start_date} to {end_date} for {listing.title}"
                ))

                review = Review.objects.create(
                    listing=listing,
                    booking=booking,
                    rating=random.randint(3, 5),
                    comment="Very nice place, would come again!"
                )
                self.stdout.write(self.style.SUCCESS(
                    f"Review for {listing.title}: {review.rating} stars"
                ))

        self.stdout.write(self.style.SUCCESS("Database seeding completed successfully!"))
