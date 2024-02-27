from enum import Enum


class LinkType(Enum):
    CLASSIC = 1
    CLASSIC_THUMB = 2
    THUMBS_LIST = 3
    VIDEO = 4


class Serp:
    def __init__(self):
        self.title = ''
        self.nb_results = 0
        self.nb_pages = 1
        self.ms = 0
        self.blocks = []
        self.links = []

    def to_dict(self):
        links = []
        for link in self.links:
            links.append(link.to_dict())

        blocks = []
        for block in self.blocks:
            blocks.append(block.to_dict())

        return {
            'title': self.title,
            'nb_results': self.nb_results,
            'nb_pages': self.nb_pages,
            'ms': self.ms,
            'blocks': blocks,
            'links': links,
        }


class Video:
    def __init__(self):
        self.title = ''
        self.url = ''
        self.company = ''

    def to_dict(self):
        return {
            'title': self.title,
            'url': self.url,
            'company': self.company,
        }


class MapLink:
    def __init__(self):
        self.title = ''
        self.url = ''

    def to_dict(self):
        return {
            'title': self.title,
            'url': self.url,
        }


class AdLink:
    def __init__(self):
        self.title = ''
        self.url = ''

    def to_dict(self):
        return {
            'title': self.title,
            'url': self.url,
        }


class OtherSearchEngineLink:
    def __init__(self):
        self.title = ''
        self.url = ''
        self.company = ''

    def to_dict(self):
        return {
            'title': self.title,
            'url': self.url,
            'company': self.company,
        }


class Block:
    def __init__(self):
        pass

    def to_dict(self):
        return {
            'type': self.__class__.__name__
        }


class Link(Block):
    def __init__(self):
        super().__init__()
        self.typeof = LinkType.CLASSIC
        self.title = None
        self.desc = None
        self.url = None
        self.extra = {}

    def to_dict(self):
        d = super().to_dict()
        d['type'] = str(self.typeof)
        d['title'] = self.title
        d['desc'] = self.desc
        d['url'] = self.url
        d['extra'] = self.extra
        return d


class GalleryBlock(Block):
    def __init__(self):
        super().__init__()
        self.suggests = []

    def to_dict(self):
        d = super().to_dict()
        d['suggests'] = self.suggests
        return d


class AdBlock(Block):
    def __init__(self):
        super().__init__()
        self.links = []

    def to_dict(self):
        d = super().to_dict()
        links = []

        for link in self.links:
            links.append(link.to_dict())

        d['links'] = links
        return d


class MapBlock(Block):
    def __init__(self):
        super().__init__()
        self.links = []

    def to_dict(self):
        d = super().to_dict()
        links = []

        for link in self.links:
            links.append(link.to_dict())

        d['links'] = links
        return d


class VideoBlock(Block):
    def __init__(self):
        super().__init__()
        self.videos = []

    def to_dict(self):
        d = super().to_dict()
        videos = []

        for video in self.videos:
            videos.append(video.to_dict())

        d['videos'] = videos
        return d


class FAQBlock(Block):
    def __init__(self):
        super().__init__()
        self.questions = []

    def to_dict(self):
        d = super().to_dict()
        d['questions'] = self.questions
        return d


class SimilarRequestBlock(Block):
    def __init__(self):
        super().__init__()
        self.requests = []

    def to_dict(self):
        d = super().to_dict()
        d['requests'] = self.requests
        return d


class RightBlock(Block):
    def __init__(self):
        super().__init__()
        self.source = 'Unknown'

    def to_dict(self):
        d = super().to_dict()
        d['source'] = self.source
        return d


class OtherSearchEngineBlock(Block):
    def __init__(self):
        super().__init__()
        self.links = []

    def to_dict(self):
        d = super().to_dict()
        links = []

        for link in self.links:
            links.append(link.to_dict())

        d['links'] = links
        return d
