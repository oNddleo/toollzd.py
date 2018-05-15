function run(){
    return new Promise((resolve, reject) => {
            setTimeout(function () {
            document.getElementsByClassName('mod-select mod-address-form-select mod-select-location-tree-1')[0].childNodes[1].click()
            document.querySelectorAll('[value="R1973756---Hồ Chí Minh"]')[0].click()
            console.log('done this step 1')
            }, 0000)
        
             setTimeout(function () {
            document.getElementsByClassName('mod-select mod-address-form-select mod-select-location-tree-2')[0].childNodes[1].click()
            document.querySelectorAll('[value="R2587287---Quận 1"]')[0].click()
            console.log('done this step 2')
            }, 3000)

            setTimeout(function () {
            document.getElementsByClassName('mod-select mod-address-form-select mod-select-location-tree-3')[0].childNodes[1].click()
            document.querySelectorAll('[value="R2587289---Phường Đa Kao"]')[0].click()
            console.log('done this step 3')
            }, 6000)   
        resolve("SUCCESS")
        })
}