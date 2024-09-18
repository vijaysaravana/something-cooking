# LRU

cache = {}

# implement LRUCache for getting stock price for a given symbol
def set_stock_price_in_cache(symbol, price):
    cache_key = "stock_price_" + symbol
    if cache_key not in cache or (cache_key in cache and cache[cache_key] != price):
        if len(cache) >= 100:
            # remove the least recently used key
            cache.pop(next(iter(cache)))
        cache[cache_key] = price

def get_stock_price_from_cache(symbol):
    print(cache)
    cache_key = "stock_price_" + symbol
    if symbol in cache:
        return cache[cache_key]
    else:
        return None