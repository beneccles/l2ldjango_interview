from django import template
from datetime import datetime

register = template.Library()

@register.filter
def date_time(value):
    if isinstance(value, datetime):
         # If we are already a datetime object, go ahead and covert to
         # Year-month-day hour-minute-second string.
         return value.strftime("%Y-%m-%d %H:%M:%S")
    else:
        # Otherwise we are a string, so we need to coverted back
        # from the ISO-8601 formate string. I could elif here to check to make sure the value
        # is in fact a string, but since we know what the two values will be,
        # I didn't think it was necessary for this excercise.

        # Note: I could also write some Regex magic to do this if we really wanted to
        # get fancy, but why do that when datetime already has the tools we need?
        convertedDateTime = datetime.fromisoformat(value)
        return convertedDateTime.strftime("%Y-%m-%d %H:%M:%S")
    
    # To better improve this in a production environment I would include error
    # handling if the values were custom user inputs instead of a dateTime object and
    # dateTime formatted string.