import React, {useState} from 'react'
import {View, StyleSheet, EdgeInsetsPropType} from 'react-native'
import {TextInput, Button} from 'react-native-paper'

function Edit(props) {

    const data = props.route.params.data;

    const [title, setTitle] = useState(data.title)
    const [body, setBody] = useState(data.body)

    const updateData = () =>{
        fetch(`http://192.168.0.4:3000/update/${data.id}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({title:title, body:body})
        })
        .then(resp => resp.json())
        .then(data => {
            props.navigation.navigate('Home', {data:data})
        })
        .catch(function(error){
            console.log("error with fetch:" + error.message);
            //throws error
            throw error;
        })

    }

    return (
        <View>
            <TextInput style = {styles.InputStyle} style ={{margin:10}}
            label = "Title"
            value = {title}
            mode="outlined"
            onChangeText = {text => setTitle(text)}/>
            <TextInput style = {styles.InputStyle} style ={{marginRight:15, marginLeft:15,marginBottom:10} }
            label = "Description"
            value = {body}
            multiline
            numberOfLines = {10}
            mode="outlined"
            onChangeText = {text => setBody(text)}/>
                            <View style={styles.btnStyle}>
                    <Button
                    style ={{margin:15, marginTop: 0}}
                    icon = "update"
                    mode="contained"
                    onPress={()=> updateData()}
                        >
                    Update Article
                    </Button>
                </View>

        </View>
        

    )
}

const styles = StyleSheet.create({
    inputStyle: {
        marginTop:10,
    },
    btnStyle: {
        flexDirection: "row",
        justifyContent: "space-evenly",
        margin: 15,
        padding: 10
    },
})

export default Edit

