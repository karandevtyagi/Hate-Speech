import Api from './APi';


// eslint-disable-next-line import/no-anonymous-default-export
export default 
function profile(data){
    return Api().post('/user',data);
 }
