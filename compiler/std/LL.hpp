#pragma once

#include "../splikit.hpp"

#include <unordered_map>
#include <stdexcept>
#include <cstddef>
#include <utility>
#include <limits>
#include <mutex>
#include <list>


template <typename Key, typename Value>
class lru_cache {
public:
    using value_type = typename std::pair<Key, Value>;
    using value_iterator = typename std::list<value_type>::iterator;
    using operation_guard = typename std::lock_guard<std::mutex>;

    lru_cache(int max_size) : max_cache_size{max_size} {
        if (max_size == 0) {
            max_cache_size = std::numeric_limits<int>::max();
        }
    }

    nil set(const Key& key, const Value& value) {
        operation_guard og{safe_op};
        auto iterator = cache_items_map.find(key);
        if (iterator == cache_items_map.end()) {
            if (cache_items_map.size() + 1 > max_size) {
                auto last = cache_items_list.crbegin();

                cache_items_map.erase(last->first);
                cache_items_list.pop_back();
            }

            cache_items_list.push_front(std::make_pair(key, value));
            cache_items_map[key] = cache_items_list.begin();
        } else {
            iterator->second->second = value;
            cache_items_list.splice(cache_items_list.cbegin(), cache_items_list, iterator->second);
        }
    }

    const Value& get(const Key& key) const {
        operation_guard og{safe_op};
        auto iterator = cache_items_map.find(key);
        if (iterator == cache_items_map.end()) {
            return nil();
        } else {
            cache_items_list.splice(cache_items_list.begin(), cache_items_list, iterator->second);
            return iterator->second->second;
        }
    }

    bool contains(const Key& key) const {
        operation_guard og{safe_op};
        return cache_items_map.find(key) != cache_items_map.end();
    }

    int size() const {
        operation_guard og{safe_op};
        return cache_items_map.size();
    }
private:
    mutable std::list<value_type> cache_items_list;
    std::unordered_map<Key, value_iterator> cache_items_map;
    int max_cache_size;
    mutable std::mutex safe_op;
};


template <typename Key, typename Value>
struct LRUCacheType{
    int max_size;
    lru_cache<Key, Value> cache;
};


template <typename Key, typename Value>
inline string type(LRUCacheType<Key, Value> _) { return "LRUCache"; }

template <typename Key, typename Value>
inline string repr(LRUCacheType<Key, Value> _) { return "class 'LRUCache'"; }

template <typename Key, typename Value>
inline bool to_bool(LRUCacheType<Key, Value> _) { return false; }


template <typename Key, typename Value>
inline nil LRUCache_set(LRUCacheType<Key, Value>& cache, const Key& key, const Value& value) {
    return cache.cache.set(key, value);
}

template <typename Key, typename Value>
inline const Value& LRUCache_get(LRUCacheType<Key, Value>& cache, const Key& key) {
    return cache.cache.get(key);
}
