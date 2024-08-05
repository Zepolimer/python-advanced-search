import re
from abc import ABC

from python_advanced_search.models.serp import (
    LinkType,
    Video,
    Link,
    MapLink,
    AdLink,
    OtherSearchEngineLink,
    GalleryBlock,
    AdBlock,
    MapBlock,
    VideoBlock,
    FAQBlock,
    SimilarRequestBlock,
    RightBlock,
    OtherSearchEngineBlock,
)
from python_advanced_search.services.serp import SerpAnalyzer


class GoogleSerpAnalyzer(SerpAnalyzer, ABC):
    def get_serp(self):
        self.serp.title = self.__get_title()
        self.serp.nb_results = self.__get_nb_results()
        self.serp.nb_pages = self.__get_nb_pages()
        self.serp.ms = self.__get_ms()
        self.serp.blocks = self.__get_blocks()
        self.serp.links = self.__get_links()
        return self.serp

    def __get_title(self):
        elms = self.document.xpath('//title')

        if len(elms) > 0:
            return elms[0].text_content()

    def __get_nb_results(self):
        elms = self.document.xpath('//*[@id="result-stats"]')

        if len(elms) > 0:
            field = elms[0].text

            if field is not None:
                numbers = re.findall("[0-9]+", field)
                if len(numbers) > 0:
                    return int(''.join(numbers))
        return 0

    def __get_nb_pages(self):
        count = self.document.xpath('count(//*[@class="AaVjTc"]//td)')
        if count > 0:
            return int(count - 2)
        return int(count)

    def __get_ms(self):
        elms = self.document.xpath('//*[@id="result-stats"]/nobr')

        if len(elms) > 0:
            field = elms[0].text

            if field is not None:
                numbers = re.findall("[0-9]+", field)
                if len(numbers) > 0:
                    return float('.'.join(numbers))
        return 0

    def __get_blocks(self):
        blocks = []

        blocks += self.__faq_blocks()
        blocks += self.__ad_blocks()
        blocks += self.__right_blocks()
        blocks += self.__video_blocks()
        blocks += self.__gallery_blocks()
        blocks += self.__similar_request_blocks()
        blocks += self.__map_blocks()
        blocks += self.__other_search_engine_blocks()

        return blocks

    def __faq_blocks(self):
        blocks = []

        faq_blocks = self.document.xpath('.//*[@id="rso"]//*[contains(@class, "AuVD")]')
        if len(faq_blocks) > 0:
            for faq_block in faq_blocks:
                block = FAQBlock()

                for question in faq_block.xpath('.//*[@jsname="Cpkphb"]//*[@class="wWOJcd"]//span'):
                    block.questions.append(question.text_content())

                blocks.append(block)
        return blocks

    def __ad_blocks(self):
        blocks = []

        ad_blocks = self.document.xpath('.//*[@id="tads" or @id="tadsb"]')
        if len(ad_blocks) > 0:
            for ad_block in ad_blocks:
                block = AdBlock()

                for ad in ad_block.xpath('.//*[@class="uEierd"]'):
                    link = AdLink()

                    elms = ad.xpath('.//*[@class="sVXRqc"]')
                    if len(elms) > 0:
                        link.url = elms[0].get('href')

                        elms = ad.xpath('.//span')
                        if len(elms) > 0:
                            link.title = elms[0].text_content()

                    block.links.append(link)

                blocks.append(block)
        return blocks

    def __right_blocks(self):
        blocks = []

        right_blocks = self.document.xpath('.//*[contains(@class, "liYKde")]')
        if len(right_blocks) > 0:
            for right_block in right_blocks:
                block = RightBlock()

                elms = right_block.xpath('.//*[@jsname="cQhrTd"]')
                if len(elms) > 0:
                    block.source = 'Google Business'

                elms = right_block.xpath('.//*[contains(@class, "ruhjFe")]')
                if len(elms) > 0:
                    block.source = elms[0].text_content()

                blocks.append(block)
        return blocks

    def __video_blocks(self):
        blocks = []

        video_blocks = self.document.xpath('.//*[contains(@class, "uVMCKf")]')
        if len(video_blocks) > 0:
            for video_block in video_blocks:
                block = VideoBlock()

                for video in video_block.xpath('.//video-voyager'):
                    v = Video()

                    video_urls = video.xpath('.//a')
                    if len(video_urls) > 0:
                        v.url = video_urls[0].get('href')

                    video_titles = video.xpath('.//span[@class="cHaqb"]')
                    if len(video_titles) > 0:
                        v.title = video_titles[0].text_content()

                    video_companys = video.xpath('.//cite')
                    if len(video_companys) > 0:
                        v.company = video_companys[0].text_content()

                    block.videos.append(v)

                blocks.append(block)
        return blocks

    def __gallery_blocks(self):
        blocks = []

        gallery_blocks = self.document.xpath('//*[@id="iur"]')
        if len(gallery_blocks) > 0:
            for gallery_block in gallery_blocks:
                block = GalleryBlock()

                for suggest in gallery_block.xpath('.//*[@class="dgdd6c"]'):
                    block.suggests.append(suggest.text_content())
                blocks.append(block)
        return blocks

    def __similar_request_blocks(self):
        blocks = []

        similar_request_blocks = self.document.xpath('.//*[@id="botstuff"]')
        if len(similar_request_blocks) > 0:
            for similar_request_block in similar_request_blocks:
                block = SimilarRequestBlock()

                for similar_request in similar_request_block.xpath('.//*[@class="y6Uyqe"]//a'):
                    block.requests.append(similar_request.text_content())

                blocks.append(block)
        return blocks

    def __map_blocks(self):
        blocks = []

        map_blocks = self.document.xpath('.//*[@jscontroller="OWrb3e"]')
        if len(map_blocks) > 0:
            for map_block in map_blocks:
                block = MapBlock()

                for link in map_block.xpath('.//*[contains(@class, "w7Dbne")]'):
                    l = MapLink()

                    link_urls = link.xpath('.//a[contains(@class, "L48Cpd")]')
                    if len(link_urls) > 0:
                        l.url = link_urls[0].get('href')

                    link_titles = link.xpath('.//span[@class="OSrXXb"]')
                    if len(link_titles) > 0:
                        l.title = link_titles[0].text_content()

                    block.links.append(l)

                blocks.append(block)
        return blocks

    def __other_search_engine_blocks(self):
        blocks = []

        other_search_engine_blocks = self.document.xpath('.//*[@id="i4BWVe"]')
        if len(other_search_engine_blocks) > 0:
            for other_search_engine_block in other_search_engine_blocks:
                block = OtherSearchEngineBlock()

                for link in other_search_engine_block.xpath('.//a[contains(@class, "t2Yvdb")]'):
                    l = OtherSearchEngineLink()
                    l.url = link.get('href')

                    link_titles = link.xpath('.//*[contains(@class, "NNFu9b")]')
                    if len(link_titles) > 0:
                        l.title = link_titles[0].text_content()

                    link_companys = link.xpath('.//span[@class="izosSe"]')
                    if len(link_companys) > 0:
                        l.company = link_companys[0].text_content()

                    block.links.append(l)

                blocks.append(block)
        return blocks

    def __get_links(self):
        links = []

        elms = self.document.xpath('//*[@id="rso"]//*[@jscontroller="SC7lYd" or contains(@class, "dFd2Tb")]')
        for e in elms:
            link = Link()

            elms = e.xpath('.//a')
            if len(elms) > 0:
                link.url = elms[0].get('href')

            elms = e.xpath('.//h3')
            if len(elms) > 0:
                link.title = elms[0].text

            elms = e.xpath('.//*[contains(@class, "VwiC3b")]')
            if len(elms) > 0:
                link.desc = elms[0].text_content()

            elms = e.xpath('.//img')
            if len(elms) > 0:
                link.typeof = LinkType.CLASSIC_THUMB
            if len(elms) > 1:
                link.typeof = LinkType.THUMBS_LIST

            css_class = e.get('class')
            if css_class:
                if 'dFd2Tb' in css_class:
                    link.typeof = LinkType.VIDEO

            elms = e.xpath('.//g-review-stars')
            if len(elms) > 0:
                spans = elms[0].getparent().xpath('./span')

                score = '-'
                if len(spans) > 0:
                    numbers = re.findall("[0-9]+", spans[0].text_content())

                    if len(numbers):
                        score = float('.'.join(numbers))
                link.extra['reviews'] = score

            elms = e.xpath('.//*[contains(@class, "Zh9jr")]/span')
            if len(elms) > 0:
                faq = []
                for elm in elms:
                    faq.append(elm.text_content())
                link.extra['faq'] = faq

            elms = e.xpath('.//*[contains(@class, "wFMWsc")]')
            if len(elms) > 0:
                data = []

                for elm in elms:
                    data.append(elm.text_content())
                link.extra['data'] = data

            elms = e.xpath('.//*[contains(@class, "HiHjCd")]/a')
            if len(elms) > 0:
                sub_links = []

                for elm in elms:
                    sub_links.append({
                        'title': elm.text_content(),
                        'url': elm.get('href')
                    })
                link.extra['sub_links'] = sub_links

            links.append(link)
        return links
