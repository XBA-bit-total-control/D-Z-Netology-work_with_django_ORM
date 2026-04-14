from datetime import datetime


class DateConverter:
   regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
   format = '%Y-%m-%d'

   def to_python(self, value: str) -> datetime:
        date = datetime.strptime(value, self.format)
        return datetime.date(date)

   def to_url(self, value: datetime) -> str:
       return value.strftime(self.format)