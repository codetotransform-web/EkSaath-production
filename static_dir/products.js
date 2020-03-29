products = [];
quantity = [];

var bag = {};

window.onload = function(){
    
    add_1 = function(k){
        var qnt = document.getElementById("qnt_"+k);
        qnt.innerHTML = parseInt(qnt.innerHTML,10)+1;
        if(products.includes(k)){
            index = products.indexOf(k);
            quantity[index] += 1;
        }
        else{
            products.push(k);
            quantity.push(1);
        } 
    }
    substract_1 = function(k){
        var qnt = document.getElementById("qnt_"+k);
        if(parseInt(qnt.innerHTML,10) > 0){
            
            qnt.innerHTML = parseInt(qnt.innerHTML,10)-1;
            index = products.indexOf(k);
            quantity[index] -= 1;
            
            if(quantity[index] == 0){
                products.splice(index,1);
                quantity.splice(index,1);
            }
        }
        
    }
    
    // k represents the initialisation of bag
    k = 0;
    add_to_bag = function(cust_id,product_id){
        
        index = products.indexOf(product_id);
        
        // if the item is in the list i.e it has more than 0 quantity
        if(index >= 0){
            
            bag[cust_id]=[];
            bag[cust_id].push([product_id , quantity[index]]);
            
            // if(k == 0){
            //     k=1;
            //     bag[cust_id]=[];
            //     bag[cust_id].push([product_id , quantity[index]]);
            // }
            // else{
            //     bag[cust_id].push([product_id , quantity[index]]);
            // }
            
            
            // Sending JSON to backend
            bag = JSON.stringify(bag);
            // console.log(bag);
            var url = '/order/set_cart?customer_id='+cust_id+'&bag='+bag;
            var req = new XMLHttpRequest();
            req.onreadystatechange = function(){
                if(this.readyState == 4 && this.status == 200){
                    // console.log("Success");
                }
            };
            
            req.open("GET",url,true);
            req.send();
            
            bag = JSON.parse(bag);
            
            document.getElementById("atb_"+product_id).innerHTML = "In Your Bag";
            document.getElementById("atb_"+product_id).disabled = true;
            document.getElementById("bag_"+cust_id).innerHTML = parseInt(document.getElementById("bag_"+cust_id).innerHTML)+1;
        }
        
        // bag[cust_id]=[];
        
        // console.log(bag[cust_id].length,bag[cust_id][0].length);
        
        
        
        // var url = '/set_cart?customer='+cust_id+'&'
    }
    
    // sc=0;
    // send_cart = function(cust_id){
    //     if(sc == 0){
    //         sc = 1;
            
    //         // bag = {
    //         //     cust : [ [product_id,quantity],[],[] ]
    //         // }
            
            
    //         // bag = JSON.stringify(bag);
    //         // console.log(bag);
    //         // var url = '/order/set_cart?customer_id='+cust_id+'&bag='+bag;
    //         // var req = new XMLHttpRequest();
    //         // req.onreadystatechange = function(){
    //         //     if(this.readyState == 4 && this.status == 200){
    //         //         console.log("Success");
    //         //     }
    //         // };
            
    //         // req.open("GET",url,true);
    //         // req.send();
    //         }
        
    // }
    

}
