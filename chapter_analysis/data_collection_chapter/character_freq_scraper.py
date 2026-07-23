from general_network.scraper import Scraper

class CharacterFreqScraper(Scraper):
    """
    Returns the characters appearing in each chapters of the book
    page: the name of the book summary page
    """
    def scrape(self, page:str) -> list[list[str]]:
        appearances = []
        request = Scraper._get_request(page)
        chapters = request.find_all("div", class_ = "pillars")
        for chapter in chapters:
            freqs = chapter.get_text().split("\n")
            appearances.append([x for x in freqs if x])
        return appearances

    def scrape_general(self, page:str):
        result = self.scrape(page)
        cleaned_result = []
        for entry in result:
            cleaned_result.append(self.clean_data(entry))
        return cleaned_result

    def save_general_data(self, page, filename):
        data = self.scrape_general(page)
        self.save_data(data, filename)


##################################################################################################
test = CharacterFreqScraper()
test.search_and_save("Summary:Warbreaker", "character_freq_data_Warbreaker.json")
test.save_general_data("Summary:Warbreaker", "character_freq_data_general_Warbreaker.json")