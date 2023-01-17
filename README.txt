Write a script collect_relationships.py that collects the relationships for a set of celebrities provided in a JSON
configuration file as follows:
python3 collect_relationships.py -c <config-file.json> -o <output_file.json>
where config-file.json contains a single JSON dictionary with the following structure (the exact path and list of
celebrities can, obviously, change):
{
“cache_dir”: “data/wdw_cache”,
“target_people”: [ “robert-downey-jr”, “justin-bieber” ]
}
In the configuration example above, we are targeting two people, "robert-downew-jr" and "justin-bieber", and
we are caching their info under data/wdw_cache.
Your script will then go and fetch the relationships for the target individuals. Note that the target people are
indicated using the identifier that follows “/dating/”. All pages visited MUST be cached in the cache directory
specified – as described in the lecture. This means that, if run twice on the same config file, it will use data
exclusively from the cache the second time.
The output format for the file is:
{
“robert-downey-jr”: [ “person-1”, “person-2”, “person-3” ],
“justin-bieber”: []
}
Where the identifiers in the list are the people the person had a relationship with. If the person has had no
relationships, then they will have an empty list.
