from django.shortcuts import render
from price_aggregator.helpers.scraper import amazon_list, ebay_list
import requests
import bs4
# Create your views here


def product_list(request):
    print(request.GET)
    if bool(request.GET):
        query = request.GET["search"]  # Retrieve the search details
        products_1 = amazon_list(query)
        products_2 = ebay_list(query)

        # print(products_1, "\n\n", products_2)

        products = []

        try:
            for product in products_1["content"]["offers"]:
                try:
                    response = requests.get(product["link"])

                    soup = bs4.BeautifulSoup(response.text, "html.parser")

                    try:
                        img = soup.find("img", id="landingImage").get("src")

                    except Exception:
                        products.append(
                            {
                                "title": product["name"],
                                "price": product["price"],
                                "url": product["link"],
                                # "img": img,
                                "source": "Amazon",
                            }
                        )

                    products.append(
                        {
                            "title": product["name"],
                            "price": product["price"],
                            "url": product["link"],
                            "img": img,
                            "source": "Amazon",
                        }
                    )
                    print("done")
                except Exception as e:
                    print(f"Error: {e}")

                if len(products) >= 4:
                    break

            print("ebay")
            for product in products_2["products"]:
                print("start")
                try:
                    products.append(
                        {
                            "title": product["title"],
                            "price": product["sale_price"],
                            "url": product["link"],
                            "img": product["image_url"],
                            "source": "Ebay",
                        }
                    )
                except Exception as e:
                    print(f"Error: {e}")

                if len(products) >= 8:
                    break
        except Exception as e:
            print("error: ", e)
            return render(
                request,
                "product_list.html",
                {
                    "products": [],
                    "error": "Error: An error occurred while fetching data.",
                },
            )
            # print()
        # print(products)
        return render(request, "product_list.html", {"products": products})
    return render(request, "product_list.html", {"products": []})
