#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import jinja2
import os
import datetime
import time

from google.appengine.api import users
from google.appengine.ext import ndb

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir))

"""class CssiUser(ndb.Model):
 CssiUser stores information about a logged-in user.

  The AppEngine users api stores just a couple of pieces of
  info about logged-in users: a unique id and their email address.

  If you want to store more info (e.g. their real name, high score,
  preferences, etc, you need to create a Datastore model like this
  example).

  first_name = ndb.StringProperty()
  last_name = ndb.StringProperty()

class SignInHandler(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    # If the user is logged in...
    if user:
      email_address = user.nickname()
      cssi_user = CssiUser.get_by_id(user.user_id())
      signout_link_html = '<a href="%s">sign out</a>' % (
          users.create_logout_url('/'))
      # If the user has previously been to our site, we greet them!
      if cssi_user:
        self.response.write('''
            Welcome %s %s (%s)! <br> %s <br>''' % (
              cssi_user.first_name,
              cssi_user.last_name,
              email_address,
              signout_link_html))
      # If the user hasn't been to our site, we ask them to sign up
      else:
        self.response.write('''
            Welcome to our site, %s!  Please sign up! <br>
            <form method="post" action="/">
            <input type="text" name="first_name">
            <input type="text" name="last_name">
            <input type="submit">
            </form><br> %s <br>
            ''' % (email_address, signout_link_html))
    # Otherwise, the user isn't logged in!
    else:
      self.response.write('''
        Please log in to use our site! <br>
        <a href="%s">Sign in</a>''' % (
          users.create_login_url('/')))

  def post(self):
    user = users.get_current_user()
    if not user:
      # You shouldn't be able to get here without being logged in
      self.error(500)
      return
    cssi_user = CssiUser(
        first_name=self.request.get('first_name'),
        last_name=self.request.get('last_name'),
        id=user.user_id())
    cssi_user.put()
    self.response.write('Thanks for signing up, %s!' %
        cssi_user.first_name)"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('home.html')
        self.response.out.write(template.render())

class StudyHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('studyCorner.html')
        self.response.out.write(template.render())

class CalendarHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('calendar.html')
        self.response.out.write(template.render())

class FlashcardsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('flashcards.html')
        self.response.out.write(template.render())

class MemoHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('memo.html')
        self.response.out.write(template.render())

class PunHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('punOfTheDay.html')
        self.response.out.write(template.render())

class TestHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('testCountdown.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([
 # ('/signin', SignInHandler),
  ('/', MainHandler),
  ('/study', StudyHandler),
  ('/calendar', CalendarHandler),
  ('/flashcards', FlashcardsHandler),
  ('/memo', MemoHandler),
  ('/pun', PunHandler),
  ('/test', TestHandler),
], debug=True)
