"""

Ler's answer some important questions that plagued humanity since.

the dawn of time with this simple XBlock.

"""

import pkg_resources
import random
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Scope, String


@XBlock.wants('user')
class WhoWhereWhyXBlock(XBlock):
    """Docstrings are excessive and bullshit. Change my mind."""

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # This field is to set a default name of the XBlock.
    # Otherwise it would default to the usage_id - a beautiful assortment
    # of letters and numbers
    display_name = String(
        display_name="Display Name",
        scope=Scope.settings,
        default="Who, Where and Why?"
    )

    # This field is present to show edX that this block shouldn't be graded.
    has_score = False

    # This field is present to define an icon
    icon_class = 'other'

    # I honestly regret googling this
    inspirational_quotes = [
        'Everything you can imagine is real. – Pablo Picasso',
        'Whatever you do, do it well. – Walt Disney',
        'What we think, we become. – Buddha',
        'Oh, the things you can find, if you don’t stay behind. – Dr. Seuss',
        'Change the world by being yourself. – Amy Poehler',
        'If you tell the truth you don’t have to remember anything.' +
        '– Mark Twain',
        'Be so good they can’t ignore you. – Steve Martin'
        ]

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # This view is for students and how it the block will be displayed in lms
    def student_view(self, context=None):
        """
        
        Primary view of the WhoWhereWhyXBlock, shown to students.
        
        when viewing courses.
        
        """
        html = self.resource_string("static/html/whowherewhy.html")
        fragment = Fragment(html.format(self=self))
        fragment.add_css(self.resource_string("static/css/whowherewhy.css"))
        fragment.add_javascript(self.resource_string(
            "static/js/src/whowherewhy.js"))
        fragment.initialize_js('WhoWhereWhyXBlock')
        return fragment

    # studio_view
    def studio_view(self, context=None):
        """Return studio view fragment."""
        fragment = super(WhoWhereWhyXBlock,
                         self).studio_view(context=context)

        # We could also move this function to a different file
        fragment.add_javascript(load("static/js/whowherewhy.js"))
        fragment.initialize_js('WhoWhereWhyXBlock')

        return fragment

    # author_view
    def author_view(self, context=None):
        """Return author view fragment on Studio."""
        # creating xblock fragment
        fragment = Fragment(u"<!-- This is the studio -->")
        fragment.add_javascript(load("static/js/whowherewhy.js"))
        fragment.initialize_js('WhoWhereWhyXBlock')

        return fragment

    # A method that returns the full name of a current authorized user.
    # Full name consists of 'First name' and 'Last name'.
    def get_current_user_full_name(self):
        """Return full name of a user."""
        user_service = self.runtime.service(self, 'user')
        xb_user = user_service.get_current_user()

        return xb_user.full_name

    # A method that returns emails of a current authorized user.
    # Emails consist of a primary and a backup one(if it was specified).
    def get_current_user_emails(self):
        """Return emails of a user."""
        # Yes, I'm aware that it's a terrible practice to constantly
        # redefine this variable and do so in multiple methods.
        # At this time, however, I'm strugling to come up with a more
        # logical and laconic way make it accessible block-wide.
        user_service = self.runtime.service(self, 'user')
        xb_user = user_service.get_current_user()

        return xb_user.emails

    # Self-explanatory, really.
    # I'd suggest this method should be a part of every program from now on
    def get_random_inspirational_quote(self):
        """Return full name of a user."""
        return random.choice(self.inspirational_quotes)

    # Handler for the 'who' button
    @XBlock.json_handler
    def who_handler(self, data, suffix=''):
        """Return the username and email of a current user."""
        # Just to show data coming in...
        assert data['requested'] == 'name'

        return {
                'name': self.get_current_user_full_name(),
                'email': self.get_current_user_emails()
        }

    # Handler for the 'where' button
    @XBlock.json_handler
    def where_handler(self, data, suffix=''):
        """Return the id of a current course."""
        # Just to show data coming in...
        assert data['requested'] == 'course'

        course_url = str(self.course_id)
        return {'course': course_url}

    # Handler for the 'why' button
    @XBlock.json_handler
    def why_handler(self, data, suffix=''):
        """Inspire user to be a better person."""
        # Just to show data coming in...
        assert data['requested'] == 'inspiration'

        return {'quote': self.get_random_inspirational_quote()}

    # This is for working in the workbench
    @staticmethod
    def workbench_scenarios():
        """Сanned scenario for display in the workbench."""
        return [
            ("WhoWhereWhyXBlock",
             """<whowherewhy/>
             """),
            ("Multiple WhoWhereWhyXBlock",
             """<vertical_demo>
                <whowherewhy/>
                <whowherewhy/>
                <whowherewhy/>
                </vertical_demo>
             """),
        ]
