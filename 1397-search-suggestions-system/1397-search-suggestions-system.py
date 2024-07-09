class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []

        prefix = ""

        for char in searchWord:
            prefix += char
            suggest = []

            for product in products:
                if product.startswith(prefix):
                    suggest.append(product)

                    if len(suggest) == 3:
                        break
            result.append(suggest)
        
        return result

        