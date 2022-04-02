# Database: sample_airbnb

## Count Specific Type of Bed
```
db.listingAndReviews.count({bed_type: "Real Bed"})
```

## Get All Type of Bed
```
db.listingAndReviews.distinct("bed_type")
```

## Total amount of price each host offer
```
db.listingAndReviews.aggregate(
    [
        {$match: {}},
        {$group: {_id: $host.host_name, total: {$sum: "$price"}}}
    ]
)
```