$(document).ready(function(){
   $(login).click(function(){
       loginname=$("#name").val();
       logincompany=$("#company").val();
       loginID=$("#PersonId").val();
       $.ajax({
          type:"GET",
          url:"/insert_person/",
          data:{name:loginname, company:logincompany, PersonId:loginID},
          dataType:"json",
          success:function(data){
              if(data)
                 self.location='login2?id='+data.name ;
              else
                 alert("不允许重复答题")
          },
          error:function(data){
          alert("cuole")}
       });
})})