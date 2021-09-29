class IPInfo:
    def __init__(self, response):
        self.success = response.get('success')
        self.message = response.get('message')
        self.fraud_score = response.get('fraud_score')
        self.country_code = response.get('country_code')
        self.region = response.get('region')
        self.city = response.get('city')
        self.ISP = response.get('ISP')
        self.ASN = response.get('ASN')
        self.organization = response.get('organization')
        self.is_crawler = response.get('is_crawler')
        self.timezone = response.get('timezone')
        self.mobile = response.get('mobile')
        self.host = response.get('host')
        self.proxy = response.get('proxy')
        self.vpn = response.get('vpn')
        self.tor = response.get('tor')
        self.active_vpn = response.get('active_vpn')
        self.active_tor = response.get('active_tor')
        self.recent_abuse = response.get('recent_abuse')
        self.bot_status = response.get('bot_status')
        self.connection_type = response.get('connection_type')
        self.abuse_velocity = response.get('abuse_velocity')
        self.zip_code = response.get('zip_code')
        self.latitude = response.get('latitude'),
        self.longitude = response.get('longitude'),
        self.request_id = response.get('request_id')

    def get_location(self):
        return self.city + " - " + self.region