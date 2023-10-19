 document.getElementsByName('gen').forEach(itr1 =>
            itr1.addEventListener('click',radioFnc)
        )


        function radioFnc(){
            document.getElementsByName('gen').forEach(itr1 => {
                if(itr1.checked){
                    document.getElementById('try1').value = itr1.value;
                } 
            });
        }


--------------------------------------------------------------------------------

        document.getElementById('deptID').addEventListener('change',slctFnc);
        function slctFnc(){
            try7.value = this.value;
        }