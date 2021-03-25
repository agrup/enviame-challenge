var axios = require("axios").default;
const fs = require('fs')

const path = 'enviameApiResponse.json'

var options = {
  method: 'POST',
  url: 'https://stage.api.enviame.io/api/s2/v2/companies/401/deliveries',
  headers: {
    Accept: 'application/json',
    'api-key': 'ea670047974b650bbcba5dd759baf1ed',
    'Content-Type': 'application/json'
  },
  data: '{\n    "shipping_order": {\n        "n_packages": "1",\n        "content_description": "ORDEN 255826267",\n        "imported_id": "255826267",\n        "order_price": "24509.0",\n        "weight": "0.98",\n        "volume": "1.0",\n        "type": "delivery"\n    },\n    "shipping_origin": {\n        "warehouse_code": "401"\n    },\n    "shipping_destination": {\n        "customer": {\n            "name": "Bernardita Tapia Riquelme",\n            "email": "b.tapia@outlook.com",\n            "phone": "977623070"\n        },\n        "delivery_address": {\n            "home_address": {\n                "place": "Puente Alto",\n                "full_address": "SAN HUGO 01324, Puente Alto, Puente Alto"\n            }\n        }\n    },\n    "carrier": {\n        "carrier_code": "BLX",\n        "tracking_number": "2"\n    }\n}'
};

axios.request(options)
.then(function (response) {
  console.log(response.data);
  fs.writeFileSync(path, JSON.stringify(response.data))
}).catch(function (error) {
  console.error(error);
});