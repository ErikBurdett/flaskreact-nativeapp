import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import Home from './components/Home';
// import ClassHome from './components/ClassHome';
import Constants from  'expo-constants'
export default function App() {
//comment for commit
//comment for commit
//comment for commit

//comment for commit


  return (
    <View style={styles.container}>
      <Home/>
      <Text>Hi</Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'lightblue',
    marginTop: Constants.statusBarHeight
  },
});
