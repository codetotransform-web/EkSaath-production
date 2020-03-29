products = [];
quantity = [];

var bag = {};

window.onload = function(){
    
    
    
    
    add_1 = function(k,cust_id){
        
        var qnt = document.getElementById("qnt_"+k);
        qnt.innerHTML = parseInt(qnt.innerHTML,10)+1;
        if(products.includes(k)){
            index = products.indexOf(k);
            quantity[index] += 1;
        }
        else{
            products.push(k);
            quantity.push(parseInt(qnt.innerHTML));
        } 
        
        // For Calculating equicvalent Price
        var per_piece_price = this.document.getElementById("price_"+k);
        var eq_price = this.document.getElementById("eq_price_"+k);
        eq_price.innerHTML = parseInt(per_piece_price.innerHTML) * parseInt(qnt.innerHTML);
        
        
        // Update the DataBase by JSON Call
        product_id = k;
        index = products.indexOf(product_id);
        bag[cust_id]=[];
        bag[cust_id].push([product_id , quantity[index]]); //k = priduct_id
        
        bag = JSON.stringify(bag);
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
    
    }
    
    substract_1 = function(k,cust_id){
        var qnt = document.getElementById("qnt_"+k);
        if(parseInt(qnt.innerHTML,10) > 1){
            new_index = -1;
            qnt.innerHTML = parseInt(qnt.innerHTML,10) - 1;
            if(products.indexOf(k) >= 0){
                index = products.indexOf(k);
                quantity[index] -= 1;
                new_index = index;
            }
            else{
                products.push(k);
                quantity.push(parseInt(qnt.innerHTML));
                new_index = products.indexOf(k);
            }
            
            
            
            
            var per_piece_price = this.document.getElementById("price_"+k);
            var eq_price = this.document.getElementById("eq_price_"+k);
            
            eq_price.innerHTML = parseInt(per_piece_price.innerHTML) * parseInt(qnt.innerHTML);
            
            if(quantity[new_index] == 0){
                products.splice(new_index,1);
                quantity.splice(new_index,1);
            }
            
            product_id = k;
            index = products.indexOf(product_id);
            bag[cust_id]=[];
            bag[cust_id].push([product_id , quantity[index]]); //k = priduct_id
                
            bag = JSON.stringify(bag);
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
            
        }
        
    }
    
    del = function(product_id,customer_id){
        
        del_item = product_id;
        console.log("entry_"+product_id , document.getElementsByClassName("entry_"+product_id)[0]);
        
        // var del_item = {customer_id : product_id};
        
        // del_item = JSON.stringify(del_item);
        var url = '/order/del_cart?customer_id='+customer_id+'&product_id='+product_id;
        var req = new XMLHttpRequest();
        req.onreadystatechange = function(){
            if(this.readyState == 4 && this.status == 200){
                // console.log("Success");
                // $("entry_"+del_item).remove();
                // elem = document.getElementById("entry_"+del_item);
                // elem.parentNode.removeChild(elem);
                
                // console.log(parseInt(document.getElementById("no_of_cart_items")));
                
                // if(parseInt(document.getElementById("no_of_cart_items")) == 0){
                //     document.getElementById("order_now_button").disabled = true;
                //     console.log(parseInt(document.getElementById("no_of_cart_items")));
                // }
                location.reload();
            }
        };
            
        req.open("GET",url,true);
        req.send();
            
        // bag = JSON.parse(bag);
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
