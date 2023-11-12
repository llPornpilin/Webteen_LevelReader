# [
#     {
#         "$group": {
#             "_id": "$userId",  # ให้รวมข้อมูลตาม id
#             "total": {"$sum": "$like"}
#         }
#     }
# ]

# result = list(collection.aggregate(pipeline))