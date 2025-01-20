from src.AdAccount import BusinessManager

# Creates a new ad-account with the given information
new_account = BusinessManager.create_ad_account(
    "onlinesales", "INR", 1, "132", "234", "234"
)

# removes a ad-account on the basis of end_advertizer_id
BusinessManager.remove_ad_account(125)

# gives a detailed info about specific ad-account
BusinessManager.get_account_info(126)
