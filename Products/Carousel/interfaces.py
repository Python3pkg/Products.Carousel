from zope import schema
from zope.interface import Interface
from zope.schema.vocabulary import SimpleVocabulary

from Products.Carousel import CarouselMessageFactory as _


class ICarousel(Interface):
    """
    A rotating display of banners.
    """

    def getSettings():
        """
        Returns an object that provides ICarouselSettings.
        """

    def getBanners():
        """
        Returns a list of objects that provide ICarouselBanner.
        """

    def width():
        """
        Return the width from the settings, or the width of the image
        """

    def height():
        """
        Return the height from the settings, or the height of the image
        """

class ICarouselSettings(Interface):
    """
    Settings for a Carousel.
    """

    enabled = schema.Bool(
        title=_('Enabled'),
        description=_('Uncheck this box to hide the Carousel temporarily.'),
        default=True,
    )

    banner_template = schema.Choice(
        title=_('Banner Type'),
        description=_('The banner is the part of the Carousel that rotates.'
            ' Choose Default for the standard Carousel banner.'),
        vocabulary='Products.Carousel.BannerTemplates',
    )

    banner_elements = schema.List(
        title=_('Banner Elements'),
        description=_('Select the elements that should be visible on the'
            ' banner. Note that custom banner types may not provide all elements.'),
        value_type=schema.Choice(
            vocabulary=SimpleVocabulary.fromItems((
                (_('Title'), 'title'),
                (_('Text'), 'text'),
                (_('Image'), 'image'),
            )),
        ),
        default=['title', 'text', 'image'],
        required=False,
    )

    width = schema.Int(
        title=_('Banner Width'),
        description=_('Enter the width of the banner in pixels. If you leave'
        ' this field blank, Carousel will use the width of the first banner.'),
        required=False,
    )

    height = schema.Int(
        title=_('Banner Height'),
        description=_('Enter the height of the banner in pixels. If you leave'
        ' this field blank, Carousel will use the height of the first banner.'),
        required=False,
    )

    pager_template = schema.Choice(
        title=_('Pager Type'),
        description=_('The pager allows user to navigate between banners.'
        ' Choose the type of pager to display, or select None for no pager.'),
        vocabulary='Products.Carousel.PagerTemplates',
    )

    element_id = schema.TextLine(
        title=_('Unique ID'),
        description=_('Enter an ID for the Carousel container element.'
        ' It can be used to apply CSS to the Carousel.'),
    )

    transition_type = schema.Choice(
        title=_('Transition'),
        vocabulary=SimpleVocabulary.fromItems((
            (_('Cross Fade'), 'fade'),
            (_('Slide'), 'slide'),
        )),
        default='fade',
    )

    transition_speed = schema.Float(
        title=_('Transition Speed'),
        description=_('Enter the speed of the transition in seconds.'),
        default=0.5,
        min=0.0,
    )

    transition_delay = schema.Float(
        title=_('Transition Delay'),
        description=_('Enter the number of seconds that Carousel should pause'
            ' between banners.'),
        default=8.0,
        min=0.0,
    )

    default_page_only = schema.Bool(
        title=_('Only display on the default item'),
        description=_('Only display the Carousel on the default item of this'
            ' folder. Otherwise, the Carousel appears on every item in'
            ' the folder.'),
        default=True,
    )

    random_order = schema.Bool(
        title=_('Random order'),
        description=_('Carousel pictures will reappear in random order on every page refresh.'),
        default=True,
    )

    lazyload = schema.Bool(
        title=_('Enabled lazily load carousel images'),
        description=_('Check this box to conserve the user and the server'
            ' bandwidth if the full carousel cycle is not shown.'),
        default=False,
    )


class ICarouselSettingsView(Interface):
    """
    Marker interface for the view that displays the Carousel settings form.
    """


class ICarouselFolder(Interface):
    """Marker for a folder that can hold Carousel banners."""


class ICarouselBanner(Interface):
    """A carousel banner which may include an image, text, and/or link."""

    def getSize(scale=None):
        """ Wraps the getSize method of the image field.
        """


class ICarouselBrowserLayer(Interface):
    """Marker applied to the request during traversal of sites that
       have Carousel installed

       Not used anymore, but here for BBB.
    """
