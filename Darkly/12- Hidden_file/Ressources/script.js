var JSSoup = require('jssoup').default;
const axios = require('axios');
require('dotenv').config()

const url = process.env.DARKLY_URL+'.hidden/'
var list = []

const sleep = async (milliseconds) => {
    return new Promise(resolve => setTimeout(resolve, milliseconds))
}

async function script (url) {
    try {
        var res = await axios.get(url)
        var soup = new JSSoup(res.data);
        var tags = soup.findAll('a')
        for (var i = 0; i < tags.length; i++) {
            await sleep(1000)
            var link = tags[i].attrs.href
            if (link === '../') ;
            else if (link[link.length - 1] === '/') 
                script(url + link)
            else {
                axios.get(url + link).then(r=>{
                    if (!list.includes(r.data)) {
                        list.push(r.data)
                        console.log({ url: url + link, content: r.data })
                    }
                }).catch(err=>{})
                
            }
        }
    }
    catch (err) {
        
    }
}

script(url)



