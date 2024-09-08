function transform(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.customer_id = values[0];
    obj.FullName = values[1];
    obj.NoOfAccounts = values[2];
    obj.customer_status = values[3];
    obj.Age_Grp = values[4];
    var jsonString = JSON.stringify(obj);
    return jsonString;
}