import pandas as pd


class BusinessManager:

    def create_ad_account(
        name, currency, timezone, end_advertizer, media_agency, partner
    ):
        try:
            ad_account = AdAccount(
                name, currency, timezone, end_advertizer, media_agency, partner
            )

            ad_account_info = [
                [
                    ad_account.name,
                    ad_account.currency,
                    ad_account.timezone_id,
                    ad_account.end_advertizer,
                    ad_account.media_agency,
                    ad_account.partner,
                ]
            ]

            df = pd.DataFrame(ad_account_info)
            df.to_csv(
                "data.csv", mode="a", index=False, header=False, lineterminator="\n"
            )

            print("AdAccount successfully created :- ")
            ad_account.print_ad_account_info()

        except Exception as e:
            print("some error occurred ", e)

    def remove_ad_account(end_advertizer_id):
        try:
            df = pd.read_csv("data.csv")
            print(df)
            df = df[df["end_advertizer"] != end_advertizer_id]
            df.to_csv("data.csv", index=False)
            print(
                f"AdAccount deleted sucessfully an ad-account with id of {end_advertizer_id}"
            )
        except Exception as e:
            print("some error occurred during deletion ", e)

    def get_account_info(end_advertizer_id):
        try:
            df = pd.read_csv("data.csv")
            result = df[df["end_advertizer"] == end_advertizer_id]

            if not result.empty:
                print(result)
            else:
                print(f"no room with end_advertizer_id : {end_advertizer_id}")
        except Exception as e:
            print("some error occurred", e)


class AdAccount:
    def __init__(
        self, name, currency, timezone_id, end_advertizer, media_agency, partner
    ):
        self.name = name
        self.currency = currency
        self.timezone_id = timezone_id
        self.end_advertizer = end_advertizer
        self.media_agency = media_agency
        self.partner = partner

    def print_ad_account_info(self):
        print(
            f""" name : {self.name}, currency:{self.currency}, timezone:{self.timezone_id},
              end_advertizer:{self.end_advertizer}, media_agency:{self.media_agency}, partner:{self.partner}"""
        )
