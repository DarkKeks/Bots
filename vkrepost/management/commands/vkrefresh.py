from django.core.management import BaseCommand

from vkrepost.apps import VkRepostConfig


class Command(BaseCommand):
    help = 'Refreshes vk posts in channels'

    def handle(self, *args, **options):
        self.stdout.write('Performing update')
        try:
            count = VkRepostConfig.worker.update()
        except Exception as err:
            self.stdout.write(self.style.ERROR('Something went wrong'))
            self.stdout.write(err)
        else:
            self.stdout.write(self.style.SUCCESS(f'Success! {count} new posts published.'))

