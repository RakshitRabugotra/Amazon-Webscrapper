"""
Amazon web-scrapper
"""
import src.util as util
import src.scrapper as scrapper
import src.db_handler as db_handler

# Fetch the settings from the settings.json file
settings = util.load_json_configuration()


# To scrap the information from the text file
def wishlist_fetch(text_file: str) -> list[str]:
    content = []
    # Try to open the file and if dit doesn't exist
    # Then return empty contents
    try:
        with open(text_file, mode='r') as file:
            content = file.read().split('\n')
    except FileNotFoundError as ff_error:
        print("[ERROR]:", ff_error)
    finally:
        # Remove all the empty string from the list, and return it
        content = list(filter(lambda x: x, content))
        return content
    

def item_information_fetch(wishlist: list) -> dict[str, dict[str, str]]:
    """
    Fetch the information about the product from the url
    """
    info = {}

    for item_url in wishlist:
        # Fetch the information from the scrapper
        info[item_url] = scrapper.scrap_information(item_url)
    # end-for

    return info



if __name__ == '__main__':
    # The driver code
    wishlist = wishlist_fetch(settings['wishlist-txt'])
    print("WISHLIST:\n", wishlist)

    # Get the information about each product by using this function
    print("The information about each of them is here!\n")
    products_information = item_information_fetch(wishlist)
    print(products_information)
