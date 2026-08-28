import type { Nota } from "@/types";
import { useLocalSearchParams, useRouter } from "expo-router";
import { useState } from "react";
import { StyleSheet, Text, TextInput, TouchableOpacity, View } from "react-native";
 
export default function CadastroScreen() {
  const router = useRouter();
  const { nota } = useLocalSearchParams<{ nota?: string }>();
  const notaExistente: Nota | null = nota ? JSON.parse(nota) : null;
 
  const [descricaoProduto, setDescricaoProduto] = useState(notaExistente?.descricaoProduto ?? '');
  const [dataCompra, setDataCompra] = useState(notaExistente?.dataCompra ?? '');
  const [loja, setLoja] = useState(notaExistente?.loja ?? '');
 
  function salvarNota() {
    if (!descricaoProduto || !loja) {
      alert('Preencha ao menos a descrição e a loja.');
      return;
    }
 
    if (notaExistente) {
      const notaAtualizada: Nota = { ...notaExistente, descricaoProduto, dataCompra, loja };
      router.push({ pathname: '/', params: { notaEditada: JSON.stringify(notaAtualizada) } });
    } else {
      const novaNota: Nota = { id: Date.now().toString(), descricaoProduto, dataCompra, loja };
      router.push({ pathname: '/', params: { novaNota: JSON.stringify(novaNota) } });
    }
  }
 
  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <TouchableOpacity onPress={() => router.back()}>
          <Text style={styles.backButton}>{'< '}</Text>
        </TouchableOpacity>
        <Text style={styles.headerTitle}>{notaExistente ? 'Editar nota' : 'Nova nota'}</Text>
      </View>
 
      <View style={{ padding: 16 }}>
        <Text style={styles.label}>Descrição do produto</Text>
        <TextInput
          style={styles.input}
          value={descricaoProduto}
          onChangeText={setDescricaoProduto}
          placeholder='Ex: Televisão 50 polegadas'
          placeholderTextColor='#5C6AA0'
        />
 
        <Text style={styles.label}>Data da compra</Text>
        <TextInput
          style={styles.input}
          value={dataCompra}
          onChangeText={setDataCompra}
          placeholder='dd/mm/aaaa'
          placeholderTextColor='#5C6AA0'
        />
 
        <Text style={styles.label}>Loja</Text>
        <TextInput
          style={styles.input}
          value={loja}
          onChangeText={setLoja}
          placeholder='Ex: Eletro Sul'
          placeholderTextColor='#5C6AA0'
        />
 
        <TouchableOpacity style={styles.saveButton} onPress={salvarNota}>
          <Text style={styles.saveButtonText}>{notaExistente ? 'Salvar alterações' : 'Salvar nota'}</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}
 
const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#0E1B33' },
  header: {
    backgroundColor: '#D85A30', padding: 16,
    flexDirection: 'row', alignItems: 'center',
  },
  backButton: { color: '#FAECE7', fontSize: 20, fontWeight: 'bold', marginRight: 8 },
  headerTitle: { color: '#FAECE7', fontSize: 20, fontWeight: 'bold' },
  label: { color: '#98A4C8', fontSize: 13, marginTop: 12, marginBottom: 4 },
  input: {
    borderWidth: 1, borderColor: '#223564', borderRadius: 8,
    padding: 10, color: '#F0F2FA', backgroundColor: '#16264A',
  },
  saveButton: {
    backgroundColor: '#D85A30', borderRadius: 8, padding: 14,
    alignItems: 'center', marginTop: 20,
  },
  saveButtonText: { color: '#FAECE7', fontWeight: 'bold', fontSize: 15 },
});
